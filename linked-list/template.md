# Linked List Template

## Basic Structure
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Common Patterns

### 1. Traversal
```python
def traverse(head):
    current = head
    while current:
        # Process current node
        current = current.next
```

### 2. Two Pointers (Fast & Slow)
```python
def two_pointers(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### 3. Reverse Linked List
```python
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

### 4. Dummy Node Pattern
```python
def with_dummy(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    # Process nodes
    return dummy.next
```

### 5. Merge Two Lists
```python
def merge(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

## Key Techniques
- Use dummy nodes to simplify edge cases
- Two pointers for cycle detection or finding middle
- Recursion for reverse or merge operations
- Track previous node for deletion/insertion

