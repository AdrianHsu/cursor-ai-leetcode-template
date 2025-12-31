# Monotonic Stack Template

## Basic Structure
```python
def monotonic_stack(nums):
    stack = []
    result = []
    
    for i, num in enumerate(nums):
        # Maintain monotonic property
        while stack and condition(stack[-1], num):
            # Process popped element
            index = stack.pop()
            result[index] = num  # or other operation
        stack.append(i)
    
    return result
```

## Common Patterns

### 1. Next Greater Element
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

### 2. Next Smaller Element
```python
def next_smaller_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result
```

### 3. Previous Greater Element
```python
def previous_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    
    return result
```

### 4. Largest Rectangle in Histogram
```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * width)
    
    return max_area
```

## Key Techniques
- Maintain increasing or decreasing order
- Store indices for distance calculations
- Process elements when popped
- Handle remaining elements after loop

