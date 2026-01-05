# Resumable Iterator Template

## Problem Overview

A **Resumable Iterator** is an iterator that can pause its iteration, save its current state, and later resume from that exact point without starting over. This is particularly useful for:

- Processing large datasets that may be interrupted
- Distributed systems where tasks can be paused and resumed
- Long-running data processing pipelines
- Handling large files or streams efficiently

## Key Components

Every resumable iterator should implement:

1. **Standard Iterator Methods:**
   - `next()`: Return the next element and advance
   - `has_next()`: Check if more elements are available

2. **State Management:**
   - `get_state()`: Return the current state (serializable)
   - `set_state(state)`: Restore iterator to a specific state

3. **Python Protocol Support:**
   - `__iter__()`: Make it iterable
   - `__next__()`: Support `for` loops


In Python, there is a distinction between an Iterable and an Iterator.

1. The Relationship
* Iterable: An object that can return an iterator (e.g., a `List, Dict, or String`). It implements `__iter__`.
* Iterator: The actual "pointer" object that moves across the data. It implements both `__iter__` and `__next__` . 
* By convention, all Iterators must also be Iterables. This is why we add `return self` in `__iter__` even though we are implementing a Iterator, not a Iterable.

Example

when you write `for x in iterator9`:, Python first calls `iter(iterator9)`. If your class doesn't have `__iter__`, Python says: "I don't know how to start a loop with this object," even though you have a `__next__` method ready to go. By adding `__iter__` that returns self, you are saying: "I am an iterator, and if you want to loop over me, just use me as I am."


## Basic Structure

```python
class ResumableIterator:
    def __init__(self, data):
        self.data = data
        self.state = initial_state
    
    def next(self):
        if not self.has_next():
            raise StopIteration
        value = self._get_current_value()
        self._advance_state()
        return value
    
    def has_next(self):
        return self._has_more_elements()
    
    def get_state(self):
        return self.state  # Must be serializable
    
    def set_state(self, state):
        self._validate_state(state)
        self.state = state
        self._reset_to_state()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.next()
```

## Variants

### 1. Resumable List Iterator

For linear data structures (lists, arrays).

**State:** Simple integer index

```python
class ResumableListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def next(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
    
    def has_next(self):
        return self.index < len(self.data)
    
    def get_state(self):
        return self.index
    
    def set_state(self, state):
        if not (0 <= state <= len(self.data)):
            raise ValueError("Invalid state")
        self.index = state
```

**Time Complexity:**
- `next()`: O(1)
- `has_next()`: O(1)
- `get_state()`: O(1)
- `set_state()`: O(1)

**Space Complexity:** O(1)

### 2. Resumable 2D Iterator

For two-dimensional structures (matrices, list of lists).

**State:** Tuple (row, col)

```python
class Resumable2DIterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = 0
        self.col = 0
        self._move_to_valid_position()
    
    def _move_to_valid_position(self):
        """Skip empty rows"""
        while self.row < len(self.matrix):
            if self.col < len(self.matrix[self.row]):
                return
            self.row += 1
            self.col = 0
    
    def next(self):
        if not self.has_next():
            raise StopIteration
        value = self.matrix[self.row][self.col]
        self.col += 1
        self._move_to_valid_position()
        return value
    
    def has_next(self):
        return self.row < len(self.matrix)
    
    def get_state(self):
        return (self.row, self.col)
    
    def set_state(self, state):
        row, col = state
        if not (0 <= row < len(self.matrix)):
            raise ValueError("Invalid row")
        if not (0 <= col <= len(self.matrix[row])):
            raise ValueError("Invalid col")
        self.row = row
        self.col = col
        self._move_to_valid_position()
```

**Time Complexity:**
- `next()`: O(1) amortized
- `has_next()`: O(1) amortized
- `get_state()`: O(1)
- `set_state()`: O(1)

**Space Complexity:** O(1)

### 3. Resumable Multi-File Iterator

For iterating over multiple files.

**State:** Dictionary {file_index, line_number, file_path}

```python
class ResumableMultiFileIterator:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.current_file_index = 0
        self.current_line_number = 0
        self.current_file_handle = None
        self._open_current_file()
    
    def _open_current_file(self):
        if self.current_file_index >= len(self.file_paths):
            return
        if self.current_file_handle:
            self.current_file_handle.close()
        file_path = self.file_paths[self.current_file_index]
        self.current_file_handle = open(file_path, 'r')
        # Skip to saved line number
        for _ in range(self.current_line_number):
            self.current_file_handle.readline()
    
    def next(self):
        if not self.has_next():
            raise StopIteration
        line = self.current_file_handle.readline()
        if line:
            self.current_line_number += 1
            return line.rstrip('\n')
        else:
            self._move_to_next_file()
            return self.next()
    
    def has_next(self):
        # Check current file or next files
        ...
    
    def get_state(self):
        return {
            'file_index': self.current_file_index,
            'line_number': self.current_line_number,
            'file_path': self.file_paths[self.current_file_index]
        }
    
    def set_state(self, state):
        file_index = state['file_index']
        line_number = state['line_number']
        if self.current_file_handle:
            self.current_file_handle.close()
        self.current_file_index = file_index
        self.current_line_number = line_number
        self._open_current_file()
```

**Time Complexity:**
- `next()`: O(1) per line
- `has_next()`: O(1)
- `get_state()`: O(1)
- `set_state()`: O(n) where n is lines to skip

**Space Complexity:** O(1)

## Design Patterns

### 1. State Serialization

States should be serializable (JSON-compatible):

```python
# Good: Simple types
state = 5  # int
state = (0, 2)  # tuple of ints
state = {'file_index': 1, 'line_number': 5}  # dict with simple values

# Bad: Non-serializable types
state = open('file.txt')  # file handle
state = lambda x: x + 1  # function
```

### 2. State Validation

Always validate state before setting:

```python
def set_state(self, state):
    # Type checking
    if not isinstance(state, expected_type):
        raise TypeError("Invalid state type")
    
    # Bounds checking
    if state < 0 or state > max_value:
        raise ValueError("State out of bounds")
    
    self.state = state
    self._reset_to_state()
```

### 3. Lazy File Handling

For file iterators, open files lazily and close when done:

```python
def _open_current_file(self):
    if self.current_file_handle:
        self.current_file_handle.close()
    self.current_file_handle = open(self.file_paths[self.current_file_index])
```

### 4. Edge Case Handling

- Empty data structures
- Out of bounds states
- Invalid state types
- End of iteration
- Irregular structures (2D with varying row lengths)

## Common Use Cases

1. **Data Processing Pipelines:** Process large datasets in chunks, save progress
2. **Distributed Systems:** Pause/resume tasks across nodes
3. **Large File Processing:** Handle files that don't fit in memory
4. **Stream Processing:** Process data streams that may be interrupted

## Testing Checklist

- [ ] Basic iteration works
- [ ] State save/restore works correctly
- [ ] State is serializable (JSON-compatible)
- [ ] Invalid states raise appropriate errors
- [ ] Edge cases handled (empty data, end of iteration)
- [ ] Python iteration protocol works (`for` loops)
- [ ] File handles are properly closed (for file iterators)
- [ ] Works with irregular structures (for 2D iterators)

## Key Techniques

- Use simple, serializable types for state (int, tuple, dict)
- Validate state before setting
- Handle edge cases (empty data, out of bounds)
- Support Python iteration protocol
- Clean up resources (close file handles)
- Move to valid positions after state changes (skip empty rows, etc.)

