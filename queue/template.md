# Queue Template

## Basic Structure
```python
from collections import deque

# Using deque (recommended)
queue = deque()
queue.append(item)      # Enqueue
item = queue.popleft()  # Dequeue
front = queue[0]        # Peek
is_empty = len(queue) == 0

# Using list (less efficient)
queue = []
queue.append(item)      # Enqueue
item = queue.pop(0)     # Dequeue (O(n) operation)
```

## Common Patterns

### 1. BFS (Breadth-First Search)
```python
from collections import deque

def bfs(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

### 2. Level Order Traversal
```python
def level_order(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### 3. Sliding Window Maximum
```python
from collections import deque

def max_sliding_window(nums, k):
    queue = deque()
    result = []
    for i, num in enumerate(nums):
        # Remove indices outside window
        while queue and queue[0] <= i - k:
            queue.popleft()
        # Remove smaller elements
        while queue and nums[queue[-1]] < num:
            queue.pop()
        queue.append(i)
        if i >= k - 1:
            result.append(nums[queue[0]])
    return result
```

## Key Techniques
- FIFO (First In First Out) property
- Use deque for O(1) operations
- Essential for BFS traversal
- Level-by-level processing

