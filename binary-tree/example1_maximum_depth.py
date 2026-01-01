"""
LeetCode 104: Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        """
        Recursive DFS approach
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


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
def test_max_depth():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.maxDepth(root1)
    assert result1 == 3, f"Test case 1 failed: got {result1}, expected 3"
    print(f"Test case 1 passed: depth = {result1}")
    
    # Test case 2
    root2 = create_tree([1, None, 2])
    result2 = solution.maxDepth(root2)
    assert result2 == 2, f"Test case 2 failed: got {result2}, expected 2"
    print(f"Test case 2 passed: depth = {result2}")
    
    # Test case 3: Empty tree
    root3 = create_tree([])
    result3 = solution.maxDepth(root3)
    assert result3 == 0, f"Test case 3 failed: got {result3}, expected 0"
    print(f"Test case 3 passed: depth = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_depth()

