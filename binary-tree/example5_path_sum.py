"""
LeetCode 112: Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The path is 5 -> 4 -> 11 -> 2, which gives 22.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false

Note: there is also Path Sum II, Path Sum III
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        """
        DFS approach: subtract node value from targetSum
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return False
        
        # If leaf node, check if remaining sum equals node value
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtrees
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))


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
def test_path_sum():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    result1 = solution.hasPathSum(root1, 22)
    assert result1 == True, f"Test case 1 failed: got {result1}, expected True"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([1, 2, 3])
    result2 = solution.hasPathSum(root2, 5)
    assert result2 == False, f"Test case 2 failed: got {result2}, expected False"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Empty tree
    root3 = create_tree([])
    result3 = solution.hasPathSum(root3, 0)
    assert result3 == False, f"Test case 3 failed: got {result3}, expected False"
    print(f"Test case 3 passed: {result3}")
    
    # Test case 4
    root4 = create_tree([1, 2])
    result4 = solution.hasPathSum(root4, 1)
    assert result4 == False, f"Test case 4 failed: got {result4}, expected False"
    print(f"Test case 4 passed: {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_path_sum()

