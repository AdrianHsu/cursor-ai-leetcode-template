"""
Resumable List Iterator

Design a resumable iterator that can pause its iteration, save its current state,
and later resume from that exact point without starting over.

Requirements:
1. Implement standard iterator methods: next() and has_next()
2. Implement state management: get_state() and set_state(state)
3. State should be serializable for storage/retrieval across sessions
4. State should track the current index position

Example Usage:
    iterator = ResumableListIterator([1, 2, 3, 4, 5])
    iterator.next()  # Returns 1
    iterator.next()  # Returns 2
    state = iterator.get_state()  # Save state (index = 2)
    
    # Later, resume from saved state
    new_iterator = ResumableListIterator([1, 2, 3, 4, 5])
    new_iterator.set_state(state)
    new_iterator.next()  # Returns 3 (resumes from index 2)
"""


class ResumableListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def next(self):
        if not self.has_next():
            # Note: we have to implement exception handling `StopIteration` anyway
            # for two cases: calling next directly, or when using __next__ underneath (eg., for loop)
            raise StopIteration("No more elements in iterator")
        
        value = self.data[self.index]
        self.index += 1
        return value
    
    def has_next(self):
        return self.index < len(self.data)
    
    def get_state(self):
        # pretty simple: check index value
        return self.index
    
    def set_state(self, state):
        """
        Restore the iterator to a specific state.
        
        Args:
            state: The index position to resume from
            
        Raises:
            ValueError: If the state is invalid (out of bounds)
        """
        if not isinstance(state, int):
            raise TypeError("State must be an integer")
        
        if state < 0 or state > len(self.data):
            raise ValueError(f"Invalid state: {state}. Must be between 0 and {len(self.data)}")
        
        self.index = state
    
    """
    In python, these double-underscore methods are called Magic Methods
    or Dunder Methods (double underscore)
    They are not meant to be called directly by a programmer 
    but are invoked automatically by Python in response to specific 
    operations or built-in functions. 

    __iter__ and __next__ (The Iterator Protocol)
    If you add these, your object becomes an Iterable. This allows your object to be used in for loops, list() conversions, or zip().

    __iter__: This is called once when the loop starts. It must return the iterator object itself.
    __next__: This is called on every single "lap" of the loop. When there is no more data, it must raise a StopIteration exception.

    When you write for x in my_obj:, Python internally does this:

    It calls it = iter(my_obj), which triggers your __iter__ method.
    It repeatedly calls next(it), which triggers your __next__ method.
    It catches the StopIteration exception to know when to stop gracefully.
    """
    def __iter__(self):
        """Make the iterator compatible with Python's iteration protocol."""
        return self
    
    def __next__(self):
        """Support Python's iteration protocol (for 'for' loops)."""
        return self.next()


# Test cases
def test_resumable_list_iterator():
    """Test the ResumableListIterator implementation."""
    print("Testing ResumableListIterator...")
    
    # Test case 1: Basic iteration
    iterator1 = ResumableListIterator([1, 2, 3, 4, 5])
    assert iterator1.next() == 1, "Test case 1a failed"
    assert iterator1.next() == 2, "Test case 1b failed"
    assert iterator1.has_next() == True, "Test case 1c failed"
    
    # Test case 2: Save and restore state
    iterator2 = ResumableListIterator([1, 2, 3, 4, 5])
    iterator2.next()  # Advance to index 1
    iterator2.next()  # Advance to index 2
    state = iterator2.get_state()  # Save state (index = 2)
    assert state == 2, "Test case 2a failed"
    
    # Create new iterator and restore state
    iterator3 = ResumableListIterator([1, 2, 3, 4, 5])
    iterator3.set_state(state)
    assert iterator3.next() == 3, "Test case 2b failed"
    assert iterator3.next() == 4, "Test case 2c failed"
    
    # Test case 3: State serialization (JSON-like)
    iterator4 = ResumableListIterator([10, 20, 30])
    iterator4.next()
    state_dict = {"index": iterator4.get_state()}  # Simulate serialization
    iterator5 = ResumableListIterator([10, 20, 30])
    iterator5.set_state(state_dict["index"])  # Simulate deserialization
    assert iterator5.next() == 20, "Test case 3 failed"
    
    # Test case 4: Edge cases
    iterator6 = ResumableListIterator([])
    assert iterator6.has_next() == False, "Test case 4a failed"
    
    iterator7 = ResumableListIterator([42])
    state_start = iterator7.get_state()
    assert state_start == 0, "Test case 4b failed"
    assert iterator7.next() == 42, "Test case 4c failed"
    assert iterator7.has_next() == False, "Test case 4d failed"
    
    # Test case 5: Invalid state handling
    iterator8 = ResumableListIterator([1, 2, 3])
    try:
        iterator8.set_state(-1)
        assert False, "Test case 5a failed: Should raise ValueError"
    except ValueError:
        pass  # Expected
    
    try:
        iterator8.set_state(10)
        assert False, "Test case 5b failed: Should raise ValueError"
    except ValueError:
        pass  # Expected
    
    # Test case 6: Python iteration protocol --> Needs __iter__ and __next__
    iterator9 = ResumableListIterator([1, 2, 3])
    result = list(iterator9)
    assert result == [1, 2, 3], "Test case 6 failed"

    # Test case 7: Python iteration protocol --> Needs __iter__ and __next__
    iterator10 = ResumableListIterator([1, 2, 3, 4])
    result = []
    for i in iterator10:
        result.append(i)
    assert result == [1, 2, 3, 4], "Test case 7 failed"   
    print("All test cases passed!")


if __name__ == "__main__":
    test_resumable_list_iterator()

