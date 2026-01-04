"""
Resumable 2D Iterator

Design a resumable iterator for two-dimensional structures like matrices or lists of lists.
The iterator should traverse elements row by row, and be able to save/resume its position.

Requirements:
1. Traverse 2D structure row by row (left to right, top to bottom)
2. Implement next(), has_next(), get_state(), set_state()
3. State should track both row and column indices
4. Handle empty rows and irregular 2D structures

Example Usage:
    matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    iterator = Resumable2DIterator(matrix)
    iterator.next()  # Returns 1
    iterator.next()  # Returns 2
    state = iterator.get_state()  # Save state (row=0, col=2)
    
    # Later, resume from saved state
    new_iterator = Resumable2DIterator(matrix)
    new_iterator.set_state(state)
    new_iterator.next()  # Returns 3 (resumes from row=0, col=2)
"""


class Resumable2DIterator:
    """
    A resumable iterator for two-dimensional data structures.
    Traverses elements row by row, tracking both row and column indices.
    
    Time Complexity:
        - next(): O(1) amortized
        - has_next(): O(1) amortized (may skip empty rows)
        - get_state(): O(1)
        - set_state(): O(1)
    
    Space Complexity: O(1) for state management
    """
    
    def __init__(self, matrix):
        """
        Initialize the iterator with a 2D structure.
        
        Args:
            matrix: List of lists or 2D array-like structure
        """
        self.matrix = matrix
        self.row = 0
        self.col = 0
        self._move_to_valid_position()
    
    def _move_to_valid_position(self):
        """
        Move to the next valid position, skipping empty rows.
        Helper method to ensure we're always at a valid position.
        """
        while self.row < len(self.matrix):
            if self.col < len(self.matrix[self.row]):
                return  # Valid position found
            # Move to next row
            self.row += 1
            self.col = 0
    
    def next(self):
        """
        Return the next element and advance the iterator.
        
        Returns:
            The next element in the 2D structure
            
        Raises:
            StopIteration: If there are no more elements
        """
        if not self.has_next():
            raise StopIteration("No more elements in iterator")
        
        value = self.matrix[self.row][self.col]
        self.col += 1
        
        # Move to next valid position
        self._move_to_valid_position()
        
        return value
    
    def has_next(self):
        """
        Check if there are more elements to iterate over.
        
        Returns:
            True if there are more elements, False otherwise
        """
        return self.row < len(self.matrix)
    
    def get_state(self):
        """
        Get the current state of the iterator.
        The state is a tuple (row, col) which is serializable.
        
        Returns:
            tuple: (row, col) - The current position indices
        """
        return (self.row, self.col)
    
    def set_state(self, state):
        """
        Restore the iterator to a specific state.
        
        Args:
            state: Tuple (row, col) representing the position to resume from
            
        Raises:
            ValueError: If the state is invalid (out of bounds)
            TypeError: If state is not a tuple
        """
        if not isinstance(state, (tuple, list)) or len(state) != 2:
            raise TypeError("State must be a tuple or list of length 2: (row, col)")
        
        row, col = state
        
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError("Row and column must be integers")
        
        if row < 0 or row >= len(self.matrix):
            raise ValueError(f"Invalid row: {row}. Must be between 0 and {len(self.matrix) - 1}")
        
        if col < 0 or col > len(self.matrix[row]):
            raise ValueError(
                f"Invalid col: {col} for row {row}. "
                f"Must be between 0 and {len(self.matrix[row])}"
            )
        
        self.row = row
        self.col = col
        self._move_to_valid_position()
    
    def __iter__(self):
        """Make the iterator compatible with Python's iteration protocol."""
        return self
    
    def __next__(self):
        """Support Python's iteration protocol (for 'for' loops)."""
        return self.next()


# Test cases
def test_resumable_2d_iterator():
    """Test the Resumable2DIterator implementation."""
    print("Testing Resumable2DIterator...")
    
    # Test case 1: Basic iteration - regular matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    iterator1 = Resumable2DIterator(matrix1)
    assert iterator1.next() == 1, "Test case 1a failed"
    assert iterator1.next() == 2, "Test case 1b failed"
    assert iterator1.next() == 3, "Test case 1c failed"
    assert iterator1.next() == 4, "Test case 1d failed"
    
    # Test case 2: Save and restore state
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    iterator2 = Resumable2DIterator(matrix2)
    iterator2.next()  # 1
    iterator2.next()  # 2
    iterator2.next()  # 3
    state = iterator2.get_state()  # Should be (1, 0) - start of row 1
    assert state == (1, 0), f"Test case 2a failed: expected (1, 0), got {state}"
    
    iterator3 = Resumable2DIterator(matrix2)
    iterator3.set_state(state)
    assert iterator3.next() == 4, "Test case 2b failed"
    assert iterator3.next() == 5, "Test case 2c failed"
    
    # Test case 3: Irregular matrix (rows of different lengths)
    matrix3 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    iterator4 = Resumable2DIterator(matrix3)
    results = []
    while iterator4.has_next():
        results.append(iterator4.next())
    assert results == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Test case 3 failed: {results}"
    
    # Test case 4: Save state in middle of row
    matrix4 = [[1, 2, 3], [4, 5, 6]]
    iterator5 = Resumable2DIterator(matrix4)
    iterator5.next()  # 1
    state_mid = iterator5.get_state()  # Should be (0, 1)
    iterator6 = Resumable2DIterator(matrix4)
    iterator6.set_state(state_mid)
    assert iterator6.next() == 2, "Test case 4 failed"
    
    # Test case 5: Matrix with empty rows
    matrix5 = [[1, 2], [], [3, 4, 5], [], [6]]
    iterator7 = Resumable2DIterator(matrix5)
    results5 = []
    while iterator7.has_next():
        results5.append(iterator7.next())
    assert results5 == [1, 2, 3, 4, 5, 6], f"Test case 5 failed: {results5}"
    
    # Test case 6: Empty matrix
    matrix6 = []
    iterator8 = Resumable2DIterator(matrix6)
    assert iterator8.has_next() == False, "Test case 6a failed"
    
    # Test case 7: Single element
    matrix7 = [[42]]
    iterator9 = Resumable2DIterator(matrix7)
    assert iterator9.next() == 42, "Test case 7a failed"
    assert iterator9.has_next() == False, "Test case 7b failed"
    
    # Test case 8: State serialization
    matrix8 = [[1, 2], [3, 4]]
    iterator10 = Resumable2DIterator(matrix8)
    iterator10.next()
    state_dict = {"position": iterator10.get_state()}  # Simulate JSON serialization
    iterator11 = Resumable2DIterator(matrix8)
    iterator11.set_state(state_dict["position"])
    assert iterator11.next() == 2, "Test case 8 failed"
    
    # Test case 9: Invalid state handling
    matrix9 = [[1, 2], [3, 4]]
    iterator12 = Resumable2DIterator(matrix9)
    try:
        iterator12.set_state((-1, 0))
        assert False, "Test case 9a failed: Should raise ValueError"
    except ValueError:
        pass  # Expected
    
    try:
        iterator12.set_state((0, 10))
        assert False, "Test case 9b failed: Should raise ValueError"
    except ValueError:
        pass  # Expected
    
    # Test case 10: Python iteration protocol
    matrix10 = [[1, 2], [3, 4]]
    iterator13 = Resumable2DIterator(matrix10)
    result = list(iterator13)
    assert result == [1, 2, 3, 4], f"Test case 10 failed: {result}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_resumable_2d_iterator()

