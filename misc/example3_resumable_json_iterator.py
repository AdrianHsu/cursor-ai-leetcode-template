"""
Resumable JSON File Iterators

Design a system of resumable iterators that can parse specific JSON files 
or a sequence of multiple JSON files. These iterators must support pausing, 
saving state, and resuming execution from the exact point of interruption.

Key Components:
1. IteratorInterface: Abstract base class defining the contract.
2. JsonFileIterator: Handles iteration over a single JSON file.
3. MultipleJsonFileIterator: Handles iteration over a list of JSON files, 
   managing transitions between them transparently.

Approach:
- State Management: 
  - For single files: Track the index within the list.
  - For multiple files: Track the current file index and the offset within that file.
- methods:
  - next(): Retrieves the next element based on current state.
  - get_state(): Returns a serializable snapshot.
  - set_state(): Restores the iterator using a saved snapshot.
"""

import json
import tempfile
import os

class IteratorInterface:
    """
    Abstract base class for resumable iterators.
    """
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError

    def get_state(self):
        raise NotImplementedError

    def set_state(self, state):
        raise NotImplementedError


class JsonFileIterator(IteratorInterface):
    """
    Iterator for a single JSON file containing a list of items.
    
    Attributes:
        data (list): The data loaded from the JSON file.
        idx (int): The current current index pointer.
    """
    
    def __init__(self, file_path):
        """
        Initialize by loading the JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        """
        # In a real scenario, consider lazy loading if files are large
        self.data = json.load(open(file_path)) 
        self.idx = 0

    def __next__(self):
        """
        Return the next element in the JSON list.
        """
        if self.idx >= len(self.data):
            raise StopIteration
        
        val = self.data[self.idx]
        self.idx += 1
        return val

    def get_state(self):
        """
        Return the current index as the state.
        """
        return self.idx

    def set_state(self, state):
        """
        Restore the iterator to a specific index.
        """
        self.idx = state


class MultipleJsonFileIterator(IteratorInterface):
    """
    Iterator that seamlessly iterates over multiple JSON files in sequence.
    
    Attributes:
        files (list): List of file paths to iterate over.
        current (int): Index of the file currently being processed.
        inner (JsonFileIterator): The iterator instance for the current file.
    """
    
    def __init__(self, file_paths):
        """
        Initialize with a list of file paths.
        """
        self.files = file_paths
        self.current = 0
        self.inner = JsonFileIterator(self.files[self.current])

    def __next__(self):
        """
        Return the next element, switching to the next file if the current one is exhausted.
        """
        try:
            return next(self.inner)
        except StopIteration:
            # Current file is done, move to the next file
            self.current += 1
            if self.current >= len(self.files):
                raise StopIteration
            
            # Initialize iterator for the new file
            self.inner = JsonFileIterator(self.files[self.current])
            return next(self.inner)

    def get_state(self):
        """
        Return a tuple representing the state: (current_file_index, inner_iterator_state).
        """
        return (self.current, self.inner.get_state())

    def set_state(self, state):
        """
        Restore the iterator state.
        
        Args:
            state (tuple): A tuple containing (file_index, inner_state).
        """
        self.current, inner_state = state
        
        # Restore the correct file iterator
        self.inner = JsonFileIterator(self.files[self.current])
        
        # Restore the position within that file
        self.inner.set_state(inner_state)


######### tests ########
def create_temp_json(data):
    """
    Helper to create a temp file with JSON data.
    Defined globally so test functions can access it.
    """
    fd, path = tempfile.mkstemp(suffix=".json")
    # os.fdopen wraps the low-level file descriptor in a Python file object
    with os.fdopen(fd, 'w') as tmp:
        json.dump(data, tmp)
    return path

def test_resumable_json_iterator():
    print("Setting up test data...")
    
    # 1. Setup Dummy Data
    data_1 = [1, 2, 3]
    data_2 = ["a", "b", "c"]
    data_3 = [{"id": 100}, {"id": 101}]
    
    file_1 = create_temp_json(data_1)
    file_2 = create_temp_json(data_2)
    file_3 = create_temp_json(data_3)
    
    all_files = [file_1, file_2, file_3]

    try:
        # --- Test Case 1: Single File Resume ---
        print("\n[Test 1] Single File Resume")
        single_iter = JsonFileIterator(file_1)
        
        assert next(single_iter) == 1
        print("  - Read first item: 1")
        
        # Save state at index 1
        state_single = single_iter.get_state()
        print(f"  - State saved: {state_single}")
        
        # Simulate crash/restart
        new_single_iter = JsonFileIterator(file_1)
        new_single_iter.set_state(state_single)
        
        # Resume
        resumed_val = next(new_single_iter)
        print(f"  - Resumed value: {resumed_val}")
        assert resumed_val == 2
        assert next(new_single_iter) == 3


        # --- Test Case 2: Multiple File Transition & Resume ---
        print("\n[Test 2] Multiple File Transition & Resume")
        multi_iter = MultipleJsonFileIterator(all_files)
        
        # Read all of file 1 (3 items) and first item of file 2
        # Expected sequence: 1, 2, 3, "a"
        results = [next(multi_iter) for _ in range(4)]
        assert results == [1, 2, 3, "a"]
        print(f"  - Read sequence: {results}")
        
        # We are now inside the second file.
        # Save state.
        state_multi = multi_iter.get_state() 
        print(f"  - State saved (file_idx, inner_idx): {state_multi}")
        
        # Simulate restart
        new_multi_iter = MultipleJsonFileIterator(all_files)
        new_multi_iter.set_state(state_multi)
        
        # Resume - expect "b" then "c"
        val1 = next(new_multi_iter)
        val2 = next(new_multi_iter)
        print(f"  - Resumed values: {val1}, {val2}")
        
        assert val1 == "b"
        assert val2 == "c"

        # Continue into file 3
        val3 = next(new_multi_iter)
        print(f"  - Crossed into file 3: {val3}")
        assert val3 == {"id": 100}

        print("\nAll tests passed successfully! ✅")

    finally:
        # Cleanup temp files
        for f in all_files:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    test_resumable_json_iterator()