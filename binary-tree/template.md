# Binary Tree Template

## Basic Structure
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Traversal Patterns

### 1. Preorder (Root -> Left -> Right)
```python
def preorder(root):
    if not root:
        return
    # Process root
    preorder(root.left)
    preorder(root.right)
```

### 2. Inorder (Left -> Root -> Right)
```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    # Process root
    inorder(root.right)
```

### 3. Postorder (Left -> Right -> Root)
```python
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    # Process root
```

### 4. Level Order (BFS)
```python
from collections import deque

def level_order(root):
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

## Common Patterns

### 1. Maximum Depth
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 2. Same Tree
```python
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))
```

### 3. Invert Tree
```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

## Key Techniques
- Recursion for tree problems
- Base case: check if root is None
- DFS for depth-first operations
- BFS for level-order operations

