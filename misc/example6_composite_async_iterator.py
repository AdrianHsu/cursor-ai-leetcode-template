"""
composite_iterator.py

Contains:
1. CompositeAsyncIterator (Manages multiple single iterators)
2. Test Runner
"""

import asyncio
import os
import tempfile

# Import the base iterator from File 1
try:
    from example5_async_iterator import AsyncFileIterator
except ImportError:
    raise ImportError("Please ensure 'example5_async_iterator.py' is in the same directory.")


class CompositeAsyncIterator:
    """
    Manages multiple AsyncFileIterators concurrently using Round-Robin.
    """
    def __init__(self, file_paths):
        # Initialize sub-iterators using the imported class
        self.iterators = {
            path: AsyncFileIterator(path) for path in file_paths
        }
        self.file_names = list(self.iterators.keys())
        self.current_index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.file_names:
            raise StopAsyncIteration

        attempts = 0
        while attempts < len(self.file_names):
            name = self.file_names[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.file_names)
            
            try:
                return await self.iterators[name].__anext__()
            except StopAsyncIteration:
                self.file_names.remove(name)
                if self.current_index >= len(self.file_names) and self.file_names:
                    self.current_index = 0
                attempts += 1
        
        raise StopAsyncIteration

    def get_state(self):
        return {
            'iterators': {
                name: it.get_state() for name, it in self.iterators.items()
            },
            'current_index': self.current_index,
            'active_files': self.file_names[:]
        }

    async def set_state(self, state):
        self.current_index = state['current_index']
        self.file_names = state['active_files']
        
        for name, sub_state in state['iterators'].items():
            if name in self.iterators:
                await self.iterators[name].set_state(sub_state)


# ==========================================
# TEST RUNNER
# ==========================================

def create_temp_file(content):
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(content)
    return path

async def test_resumable_async_iterator():
    print("Running Composite Iterator Test...")
    
    file_1 = create_temp_file("A1\nA2\nA3\n")
    file_2 = create_temp_file("B1\nB2\nB3\n")
    files_list = [file_1, file_2]

    try:
        # Step 1: Read partial data
        composite_iter = CompositeAsyncIterator(files_list)
        
        r1 = await composite_iter.__anext__() # A1
        r2 = await composite_iter.__anext__() # B1
        r3 = await composite_iter.__anext__() # A2
        
        print(f"  Read sequence: {r1}, {r2}, {r3}")
        assert r1 == "A1" and r2 == "B1" and r3 == "A2"

        # Step 2: Capture State (Paused at B2)
        saved_state = composite_iter.get_state()
        print(f"  State captured.")

        # Step 3: Resume in new instance
        new_iter = CompositeAsyncIterator(files_list)
        await new_iter.set_state(saved_state)
        
        r4 = await new_iter.__anext__()
        r5 = await new_iter.__anext__()
        r6 = await new_iter.__anext__()
        
        print(f"  Resumed sequence: {r4}, {r5}, {r6}")
        assert r4 == "B2" and r5 == "A3" and r6 == "B3"
        
        print("All tests passed! ✅")

    finally:
        if os.path.exists(file_1): os.remove(file_1)
        if os.path.exists(file_2): os.remove(file_2)

if __name__ == "__main__":
    asyncio.run(test_resumable_async_iterator())