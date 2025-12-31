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

