# Backtracking Template

## Basic Structure
```python
def backtrack(candidate, ...):
    if is_solution(candidate):
        result.append(candidate[:])  # Make a copy
        return
    
    for next_candidate in get_candidates():
        if is_valid(next_candidate):
            candidate.append(next_candidate)  # Make choice
            backtrack(candidate, ...)         # Recurse
            candidate.pop()                   # Undo choice
```

## Why `[:]`?
The reason is that Python lists are **mutable objects**, and variables in Python hold **references** (pointers) to those objects, not the actual values.

Here is the breakdown of why `curr` fails and `curr[:]` works:

### 1. The Short Answer

* **`self.results.append(curr)`**: You are appending a **reference** (a link) to the `curr` list. Since you reuse the exact same `curr` list throughout the entire recursion (appending and popping), `results` will end up containing multiple links to the *same* list. By the time the algorithm finishes, that list is empty (because you popped everything off).
* **`self.results.append(curr[:])`**: You are creating a **shallow copy** (a snapshot) of the list at that specific moment. You store this new, independent list in `results`. Modifications to `curr` later do not affect this stored copy.

---

### 2. Step-by-Step Visualization

Let's trace `nums = [1, 2]`.

#### Scenario A: The Wrong Way (`append(curr)`)

1. **Start**: `curr` is created at memory address `0x123`.
2. **Find [1, 2]**: `curr` is `[1, 2]`.
* We append `curr` to results.
* `results = [ <pointer to 0x123> ]`


3. **Backtrack**: We `pop()`. `curr` at `0x123` becomes `[1]`.
* *Note: The item inside `results` also changes to `[1]` because it points to `0x123`.*


4. **Find [2, 1]**: `curr` at `0x123` becomes `[2, 1]`.
* We append `curr` to results.
* `results = [ <pointer to 0x123>, <pointer to 0x123> ]`


5. **Finish**: The recursion ends. We backtrack all the way to the root.
* `curr` at `0x123` is now `[]` (empty).


6. **Final Output**:
* `results` looks at `0x123` twice.
* Output: `[[], []]`



#### Scenario B: The Correct Way (`append(curr[:])`)

1. **Start**: `curr` is at `0x123`.
2. **Find [1, 2]**: `curr` is `[1, 2]`.
* `curr[:]` creates a **new list** at memory `0x456` containing `[1, 2]`.
* `results = [ <pointer to 0x456> ]`


3. **Backtrack**: We `pop()`. `curr` at `0x123` becomes `[1]`.
* *Note: The list at `0x456` is untouched.*


4. **Find [2, 1]**: `curr` is `[2, 1]`.
* `curr[:]` creates a **new list** at memory `0x789` containing `[2, 1]`.
* `results = [ <pointer to 0x456>, <pointer to 0x789> ]`


5. **Finish**: `curr` becomes `[]`.
6. **Final Output**:
* `results` holds pointers to the copies.
* Output: `[[1, 2], [2, 1]]`



### Summary

In Python backtracking, always use one of these methods to store a mutable result:

1. `curr[:]` (Slicing - most pythonic)
2. `curr.copy()` (Explicit copy)
3. `list(curr)` (Constructor copy)

## Common Patterns

### 1. Permutations
```python
def permute(nums):
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result
```

### 2. Combinations
```python
def combine(n, k):
    result = []
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(1, [])
    return result
```

### 3. Subsets
```python
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

### 4. N-Queens
```python
def solve_n_queens(n):
    result = []
    board = ['.' * n for _ in range(n)]
    
    def is_safe(row, col):
        # Check column, diagonals
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True
    
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                backtrack(row + 1)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
    
    backtrack(0)
    return result
```

## Key Techniques
- Make choice, recurse, undo choice
- Prune invalid paths early
- Copy result when adding to output
- Use sets/arrays to track used elements

