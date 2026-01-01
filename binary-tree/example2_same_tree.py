"""
LeetCode 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False

        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

# Helper function to create tree from list
def create_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    from collections import deque
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        node = queue.popleft()
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
def test_same_tree():
    solution = Solution()
    
    # Test case 1
    p1 = create_tree([1, 2, 3])
    q1 = create_tree([1, 2, 3])
    result1 = solution.isSameTree(p1, q1)
    assert result1 == True, f"Test case 1 failed: got {result1}"
    print("Test case 1 passed: Same trees")
    
    # Test case 2
    p2 = create_tree([1, 2])
    q2 = create_tree([1, None, 2])
    result2 = solution.isSameTree(p2, q2)
    assert result2 == False, f"Test case 2 failed: got {result2}"
    print("Test case 2 passed: Different structures")
    
    # Test case 3
    p3 = create_tree([1, 2, 1])
    q3 = create_tree([1, 1, 2])
    result3 = solution.isSameTree(p3, q3)
    assert result3 == False, f"Test case 3 failed: got {result3}"
    print("Test case 3 passed: Different values")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_same_tree()

