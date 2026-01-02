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

### 3. Largest Rectangle in Histogram
```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1 # why? see note
            max_area = max(max_area, h * width)
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * width)
    
    return max_area
```

The geometric meaning of the code `i - stack[-1] - 1` is:

$$(\text{Index of the first smaller bar to the right}) - (\text{Index of the first smaller bar to the left}) - 1$$


* i (Right Limit): The "wall" on the right (Exclusive; it is not included in the width).
* stack[-1] (Left Limit): The "wall" on the left (Exclusive; it is not included in the width).
* Why subtract 1? Because both indices represent "walls" (bars that are shorter than the current height). The actual rectangle exists between these two walls.

Why are there gaps in the Stack indices?Because the "taller bars" that were in between (like the 6 in the example) have been popped, but their positions are still occupiable by the current bar (height 5). stack[-1] faithfully records the position of the first bar on the left that actually blocks the extension.

## Key Techniques
- Maintain increasing or decreasing order
- Store indices for distance calculations
- Process elements when popped
- Handle remaining elements after loop

