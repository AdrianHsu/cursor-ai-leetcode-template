"""
Resumable Multi-File Iterator

Design a resumable iterator for iterating over multiple files, especially useful
for large datasets split across files. The iterator should be able to pause,
save its state (current file and position within that file), and resume later.

Requirements:
1. Iterate over multiple files sequentially
2. Track current file index and position within that file
3. Implement next(), has_next(), get_state(), set_state()
4. Handle file opening/closing efficiently
5. State should be serializable (file path and line/byte position)

Example Usage:
    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
    iterator = ResumableMultiFileIterator(file_paths)
    iterator.next()  # Returns first line from file1.txt
    iterator.next()  # Returns second line from file1.txt
    state = iterator.get_state()  # Save state
    
    # Later, resume from saved state
    new_iterator = ResumableMultiFileIterator(file_paths)
    new_iterator.set_state(state)
    new_iterator.next()  # Resumes from saved position
"""

import os
from typing import List, Optional


class ResumableMultiFileIterator:
    """
    A resumable iterator for multiple files.
    Tracks the current file index and line number within that file.
    
    Time Complexity:
        - next(): O(1) per line read
        - has_next(): O(1)
        - get_state(): O(1)
        - set_state(): O(n) where n is the number of lines to skip
    
    Space Complexity: O(1) for state management, O(1) for file handles
    """
    
    def __init__(self, file_paths: List[str]):
        """
        Initialize the iterator with a list of file paths.
        
        Args:
            file_paths: List of file paths to iterate over
        """
        self.file_paths = file_paths
        self.current_file_index = 0
        self.current_line_number = 0
        self.current_file_handle: Optional = None
        self._open_current_file()
    
    def _open_current_file(self):
        """Open the current file and reset line number."""
        if self.current_file_index >= len(self.file_paths):
            return
        
        # Close previous file if open
        if self.current_file_handle:
            self.current_file_handle.close()
        
        file_path = self.file_paths[self.current_file_index]
        if os.path.exists(file_path):
            self.current_file_handle = open(file_path, 'r', encoding='utf-8')
            # Skip to the saved line number if resuming
            for _ in range(self.current_line_number):
                try:
                    self.current_file_handle.readline()
                except:
                    break
        else:
            # File doesn't exist, move to next file
            self.current_file_index += 1
            self.current_line_number = 0
            self.current_file_handle = None
            if self.current_file_index < len(self.file_paths):
                self._open_current_file()
    
    def _move_to_next_file(self):
        """Move to the next file, closing the current one."""
        if self.current_file_handle:
            self.current_file_handle.close()
            self.current_file_handle = None
        
        self.current_file_index += 1
        self.current_line_number = 0
        
        if self.current_file_index < len(self.file_paths):
            self._open_current_file()
    
    def next(self) -> str:
        """
        Return the next line from the current file.
        Automatically moves to the next file when the current one is exhausted.
        
        Returns:
            str: The next line (with newline character)
            
        Raises:
            StopIteration: If there are no more lines in any file
        """
        if not self.has_next():
            raise StopIteration("No more lines in any file")
        
        if not self.current_file_handle:
            self._move_to_next_file()
            if not self.has_next():
                raise StopIteration("No more lines in any file")
        
        line = self.current_file_handle.readline()
        
        if line:  # Line read successfully
            self.current_line_number += 1
            return line.rstrip('\n')  # Return without trailing newline
        else:  # End of current file
            self._move_to_next_file()
            if self.has_next():
                return self.next()  # Recursively get next line from next file
            else:
                raise StopIteration("No more lines in any file")
    
    def has_next(self) -> bool:
        """
        Check if there are more lines to read from any file.
        
        Returns:
            bool: True if there are more lines, False otherwise
        """
        # Check if we have a valid file index
        if self.current_file_index >= len(self.file_paths):
            return False
        
        # Check if current file has more lines
        if self.current_file_handle:
            # Save current position
            current_pos = self.current_file_handle.tell()
            # Try to read a line
            line = self.current_file_handle.readline()
            # Restore position
            self.current_file_handle.seek(current_pos)
            
            if line:
                return True
        
        # Check if there are more files
        for i in range(self.current_file_index + 1, len(self.file_paths)):
            file_path = self.file_paths[i]
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        if f.readline():
                            return True
                except:
                    continue
        
        return False
    
    def get_state(self) -> dict:
        """
        Get the current state of the iterator.
        The state is a dictionary containing file index and line number.
        
        Returns:
            dict: {'file_index': int, 'line_number': int, 'file_path': str}
        """
        file_path = (
            self.file_paths[self.current_file_index]
            if self.current_file_index < len(self.file_paths)
            else None
        )
        return {
            'file_index': self.current_file_index,
            'line_number': self.current_line_number,
            'file_path': file_path
        }
    
    def set_state(self, state: dict):
        """
        Restore the iterator to a specific state.
        
        Args:
            state: Dictionary with 'file_index' and 'line_number' keys
            
        Raises:
            ValueError: If the state is invalid
            TypeError: If state is not a dictionary
        """
        if not isinstance(state, dict):
            raise TypeError("State must be a dictionary")
        
        file_index = state.get('file_index')
        line_number = state.get('line_number', 0)
        
        if file_index is None:
            raise ValueError("State must contain 'file_index' key")
        
        if not isinstance(file_index, int) or file_index < 0:
            raise ValueError(f"Invalid file_index: {file_index}. Must be a non-negative integer")
        
        if file_index >= len(self.file_paths):
            raise ValueError(
                f"Invalid file_index: {file_index}. "
                f"Must be between 0 and {len(self.file_paths) - 1}"
            )
        
        if not isinstance(line_number, int) or line_number < 0:
            raise ValueError(f"Invalid line_number: {line_number}. Must be a non-negative integer")
        
        # Close current file if open
        if self.current_file_handle:
            self.current_file_handle.close()
        
        self.current_file_index = file_index
        self.current_line_number = line_number
        self._open_current_file()
    
    def __iter__(self):
        """Make the iterator compatible with Python's iteration protocol."""
        return self
    
    def __next__(self):
        """Support Python's iteration protocol (for 'for' loops)."""
        return self.next()
    
    def __del__(self):
        """Cleanup: close file handle when iterator is destroyed."""
        if self.current_file_handle:
            self.current_file_handle.close()


# Test cases
def test_resumable_multi_file_iterator():
    """Test the ResumableMultiFileIterator implementation."""
    print("Testing ResumableMultiFileIterator...")
    
    # Create temporary test files
    test_dir = "/tmp/resumable_iterator_test"
    os.makedirs(test_dir, exist_ok=True)
    
    file1_path = os.path.join(test_dir, "file1.txt")
    file2_path = os.path.join(test_dir, "file2.txt")
    file3_path = os.path.join(test_dir, "file3.txt")
    
    # Create test files
    with open(file1_path, 'w') as f:
        f.write("line1_file1\nline2_file1\nline3_file1\n")
    
    with open(file2_path, 'w') as f:
        f.write("line1_file2\nline2_file2\n")
    
    with open(file3_path, 'w') as f:
        f.write("line1_file3\n")
    
    file_paths = [file1_path, file2_path, file3_path]
    
    try:
        # Test case 1: Basic iteration
        iterator1 = ResumableMultiFileIterator(file_paths)
        assert iterator1.next() == "line1_file1", "Test case 1a failed"
        assert iterator1.next() == "line2_file1", "Test case 1b failed"
        assert iterator1.next() == "line3_file1", "Test case 1c failed"
        assert iterator1.next() == "line1_file2", "Test case 1d failed"
        
        # Test case 2: Save and restore state
        iterator2 = ResumableMultiFileIterator(file_paths)
        iterator2.next()  # line1_file1
        iterator2.next()  # line2_file1
        state = iterator2.get_state()
        assert state['file_index'] == 0, "Test case 2a failed"
        assert state['line_number'] == 2, "Test case 2b failed"
        
        iterator3 = ResumableMultiFileIterator(file_paths)
        iterator3.set_state(state)
        assert iterator3.next() == "line3_file1", "Test case 2c failed"
        assert iterator3.next() == "line1_file2", "Test case 2d failed"
        
        # Test case 3: Resume from different file
        iterator4 = ResumableMultiFileIterator(file_paths)
        iterator4.next()  # line1_file1
        iterator4.next()  # line2_file1
        iterator4.next()  # line3_file1
        iterator4.next()  # line1_file2
        state_file2 = iterator4.get_state()
        
        iterator5 = ResumableMultiFileIterator(file_paths)
        iterator5.set_state(state_file2)
        assert iterator5.next() == "line2_file2", "Test case 3 failed"
        
        # Test case 4: Iterate through all files
        iterator6 = ResumableMultiFileIterator(file_paths)
        all_lines = []
        while iterator6.has_next():
            all_lines.append(iterator6.next())
        
        expected = [
            "line1_file1", "line2_file1", "line3_file1",
            "line1_file2", "line2_file2",
            "line1_file3"
        ]
        assert all_lines == expected, f"Test case 4 failed: {all_lines}"
        
        # Test case 5: State serialization (JSON-like)
        iterator7 = ResumableMultiFileIterator(file_paths)
        iterator7.next()
        state_json = iterator7.get_state()  # Can be serialized to JSON
        iterator8 = ResumableMultiFileIterator(file_paths)
        iterator8.set_state(state_json)
        assert iterator8.next() == "line2_file1", "Test case 5 failed"
        
        # Test case 6: Invalid state handling
        iterator9 = ResumableMultiFileIterator(file_paths)
        try:
            iterator9.set_state({'file_index': -1})
            assert False, "Test case 6a failed: Should raise ValueError"
        except ValueError:
            pass  # Expected
        
        try:
            iterator9.set_state({'file_index': 100})
            assert False, "Test case 6b failed: Should raise ValueError"
        except ValueError:
            pass  # Expected
        
        # Test case 7: Python iteration protocol
        iterator10 = ResumableMultiFileIterator([file1_path])
        result = list(iterator10)
        assert result == ["line1_file1", "line2_file1", "line3_file1"], f"Test case 7 failed: {result}"
        
        print("All test cases passed!")
    
    finally:
        # Cleanup test files
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)
        if os.path.exists(test_dir):
            os.rmdir(test_dir)


if __name__ == "__main__":
    test_resumable_multi_file_iterator()

