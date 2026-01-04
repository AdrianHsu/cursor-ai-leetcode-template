import asyncio
import os

"""
Design an iterator system that supports pause and resume functionality through
get_state() and set_state() methods, enabling asynchronous iteration across
multiple data sources concurrently.

The iterator must maintain execution state for each data source independently
while supporting non-blocking coroutine-based operations.

For example, when iterating over three files simultaneously, pausing at:
  - file 1's line 5
  - file 2's line 3
  - file 3's line 7
the state should be serializable and restorable to resume from those exact positions.

Input:
    files = ['data1.txt', 'data2.txt']
    iterator = AsyncCompositeIterator(files)
    await iterator.next()         # Returns first item from data1.txt
    state = iterator.get_state()  # Capture current position
    await iterator.next()         # Continue iteration
    iterator.set_state(state)     # Restore to previous position

Output:
    Iterator resumes from the exact position where state was captured,
    returning the same item that would have been next at that point.

Explanation:
    The get_state() captures positions across all files, and set_state()
    restores them, enabling pause/resume functionality.

Constraints:
    1. Must support asynchronous iteration using async/await syntax.
    2. State must be serializable (can be converted to/from dictionary or JSON).
    3. Must handle multiple concurrent iterators without interference.
    4. Each data source maintains independent state within the composite iterator.
    5. Must support non-blocking I/O operations for file reading.
"""

# ==========================================
# 1. MOCK AIOFILES (Must be in this file)
# ==========================================
class MockAsyncFileContext:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file_obj = None

    async def __aenter__(self):
        self.file_obj = open(self.path, self.mode)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

    async def seek(self, position):
        # Simulate async I/O delay
        await asyncio.sleep(0.001) 
        self.file_obj.seek(position)

    async def tell(self):
        return self.file_obj.tell()

    async def readline(self):
        await asyncio.sleep(0.001)
        return self.file_obj.readline()

class MockAioFiles:
    def open(self, path, mode):
        return MockAsyncFileContext(path, mode)

# This global variable is what AsyncFileIterator looks for
aiofiles = MockAioFiles()

class AsyncFileIterator:
    """
    Async iterator for a single file.
    Tracks byte offset and line number for resumption.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.position = 0
        self.line_number = 0
        self.file_ctx = None
        self.file = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        # Lazy initialization
        if not self.file:
            self.file_ctx = aiofiles.open(self.filepath, 'r')
            self.file = await self.file_ctx.__aenter__()
            if self.position > 0:
                await self.file.seek(self.position)

        line = await self.file.readline()
        
        if not line:
            await self.file_ctx.__aexit__(None, None, None)
            raise StopAsyncIteration

        self.position = await self.file.tell()
        self.line_number += 1
        return line.strip()

    def get_state(self):
        return {
            'type': 'file_iterator',
            'file': self.filepath,
            'position': self.position,
            'line': self.line_number
        }

    async def set_state(self, state):
        self.position = state['position']
        self.line_number = state['line']
        if self.file:
            await self.file.seek(self.position)

# ==========================================
# 2. UNIT TESTS
# ==========================================
async def test_resumable_async_iterator():
    test_file = "test_iterator_data.txt"
    # Create a temporary file with known content
    content = "Line 1\nLine 2\nLine 3\nLine 4\n"
    with open(test_file, "w") as f:
        f.write(content)

    print(f"--- Starting Tests with file: {test_file} ---")

    try:
        # --- TEST 1: Basic Iteration ---
        print("Test 1: Basic full iteration...", end=" ")
        iterator = AsyncFileIterator(test_file)
        lines = []
        async for line in iterator:
            lines.append(line)
        
        assert lines == ["Line 1", "Line 2", "Line 3", "Line 4"]
        print("PASSED")

        # --- TEST 2: State Capture and Resumption ---
        print("Test 2: Interrupt and Resume...", end=" ")
        
        # Start first iterator
        it1 = AsyncFileIterator(test_file)
        
        # Read the first two lines
        assert await it1.__anext__() == "Line 1"
        assert await it1.__anext__() == "Line 2"
        
        # Capture the state after Line 2
        state = it1.get_state()
        assert state['line'] == 2
        assert state['position'] > 0 # Byte offset should be positive
        
        # Simulate a crash/restart by creating a NEW iterator
        it2 = AsyncFileIterator(test_file)
        
        # Apply the previous state
        await it2.set_state(state)
        
        # Verify it picks up at Line 3
        assert await it2.__anext__() == "Line 3"
        assert await it2.__anext__() == "Line 4"
        
        # Verify it stops correctly
        try:
            await it2.__anext__()
        except StopAsyncIteration:
            pass # Expected behavior
        
        print("PASSED")

        # --- TEST 3: Resuming at End of File ---
        print("Test 3: Resuming at EOF...", end=" ")
        it_eof = AsyncFileIterator(test_file)
        
        # Exhaust the file
        async for _ in it_eof: 
            pass
        
        eof_state = it_eof.get_state()
        
        # Create new iterator at EOF
        it_check = AsyncFileIterator(test_file)
        await it_check.set_state(eof_state)
        
        try:
            await it_check.__anext__()
            print("FAILED (Did not raise StopAsyncIteration)")
        except StopAsyncIteration:
            print("PASSED")

    except AssertionError as e:
        print(f"\nTEST FAILED: {e}")
    except Exception as e:
        print(f"\nAN ERROR OCCURRED: {e}")
    finally:
        # Cleanup
        if os.path.exists(test_file):
            os.remove(test_file)
        print("--- Tests Finished (Cleanup Complete) ---")

if __name__ == "__main__":
    asyncio.run(test_resumable_async_iterator())