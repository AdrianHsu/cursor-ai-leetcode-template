# Stack Template

## Basic Structure
```python
# Using list as stack
stack = []
stack.append(item)      # Push
item = stack.pop()      # Pop
top = stack[-1]         # Peek
is_empty = len(stack) == 0
```

## Common Patterns

### 1. Valid Parentheses
```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack
```

### 2. Next Greater Element
```python
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

### 3. Daily Temperatures
```python
def daily_temperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result
```

### 4. Evaluate Expression
```python
def evaluate(expression):
    stack = []
    for token in expression:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(a // b)
        else:
            stack.append(int(token))
    return stack[0]
```

## Key Techniques
- LIFO (Last In First Out) property
- Use for matching pairs (parentheses, brackets)
- Monotonic stack for next greater/smaller problems
- Track indices for distance calculations

