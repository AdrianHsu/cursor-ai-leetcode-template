# Two Pointers Template

## Basic Patterns

### 1. Opposite Ends (Array/String)
```python
def opposite_ends(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if condition:
            left += 1
        else:
            right -= 1
    return result
```

### 2. Same Direction (Sliding Window)
```python
def same_direction(arr):
    left = 0
    for right in range(len(arr)):
        # Expand window
        while condition:
            # Shrink window
            left += 1
        # Process current window
```

### 3. Fast and Slow (Linked List)
```python
def fast_slow(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

## Common Use Cases

### 1. Two Sum (Sorted Array)
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Remove Duplicates
```python
def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

### 3. Container With Most Water
```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_water = max(max_water, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
```

## Key Techniques
- Opposite ends for sorted arrays
- Same direction for sliding windows
- Fast/slow for cycle detection
- Move pointer based on condition

