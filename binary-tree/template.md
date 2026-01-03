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

## LCA

The function definition is technically: 
`"Return the LCA if it exists in this subtree; 
otherwise, return the node (p or q) if it exists in this subtree."`

It is not only `"Return the LCA if it exists in this subtree"` --> It has double meaning.

When the code hits if root == p or root == q: return root, it stops searching that branch. 
You might worry: "Wait, if I stop at p, how do I know if q is inside p's subtree?"

The answer: there are two scenarios here, and the logic handles both perfectly already.

* Scenario A: q is inside p's subtree

If root is p, and q is somewhere below p:

We return p immediately. We don't visit the children of p. We effectively "ignore" finding q. This is correct **because hypothetically if q is a descendant of p, then p IS the LCA --> Done**. We return p up the stack. The top-level caller receives p, which is the correct LCA.

* Scenario B: q is in a completely different branch. 

If root is p, and q is in the neighbor's right subtree: 

We return p immediately. The recursion unwinds to a common ancestor. Parent receives p from its left child. Parent searches its right child and eventually finds q (returning q up). Parent sees that it received a Left result (p) and a Right result (q).

Crucial Step: Because both sides returned something, Parent knows "I am the split point". Parent returns itself.
Hence, even if we don't look at nodes below `p`, as the parent will find q (under such case) so returning `p` is effectively the same result.

However, the reason why it worked is because of 1 constraint: "All Node.val are unique... p and q will exist in the tree."

If q = 9 (and 9 is not in the tree), the standard algorithm would indeed return 5, not None.

And technically, that would be wrong if we require both nodes to exist to have an LCA.

Because the problem guarantees q exists, the algorithm is allowed to be "lazy."


--

## Key Techniques
- Recursion for tree problems
- Base case: check if root is None
- DFS for depth-first operations
- BFS for level-order operations

