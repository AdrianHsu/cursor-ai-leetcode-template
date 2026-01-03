"""
LeetCode 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        """
        Recursive DFS approach
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return 0
        
        # If both children exist, take minimum
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        # If only one child exists, must go that way
        if root.left:
            return 1 + self.minDepth(root.left)
        
        if root.right:
            return 1 + self.minDepth(root.right)
        
        # Leaf node
        return 1


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
def test_minimum_depth():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.minDepth(root1)
    assert result1 == 2, f"Test case 1 failed: got {result1}, expected 2"
    print(f"Test case 1 passed: depth = {result1}")
    
    # Test case 2
    root2 = create_tree([2, None, 3, None, 4, None, 5, None, 6])
    result2 = solution.minDepth(root2)
    assert result2 == 5, f"Test case 2 failed: got {result2}, expected 5"
    print(f"Test case 2 passed: depth = {result2}")
    
    # Test case 3: Single node
    root3 = create_tree([1])
    result3 = solution.minDepth(root3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: depth = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_minimum_depth()

