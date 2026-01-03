"""
LeetCode 337: House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place form a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        # """
        # DFS / Post-order Traversal approach
        # Time Complexity: O(n) - visit every node once
        # Space Complexity: O(h) - recursion stack height
        # """
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            # Post-order traversal: process children first
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Option 1: Rob this node. 
            # If we rob this node, we cannot rob its immediate children.
            rob_this = node.val + left[1] + right[1]
            
            # Option 2: Do not rob this node.
            # If we skip this node, we are free to rob or skip the children (take max of each).
            skip_this = max(left) + max(right)
            
            # Return tuple: (max money if we rob current, max money if we skip current)
            return (rob_this, skip_this)

        result = dfs(root)
        return max(result)

# Test cases
def test_rob_iii():
    solution = Solution()
    
    # Helper to build simple tree for testing: [3, 2, 3, null, 3, null, 1]
    #       3
    #      / \
    #     2   3
    #      \   \
    #       3   1
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(1)
    
    result1 = solution.rob(root1)
    assert result1 == 7, f"Test case 1 failed: got {result1}, expected 7"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2: [3, 4, 5, 1, 3, null, 1]
    #       3
    #      / \
    #     4   5
    #    / \   \
    #   1   3   1
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(1)
    
    result2 = solution.rob(root2)
    assert result2 == 9, f"Test case 2 failed: got {result2}, expected 9"
    print(f"Test case 2 passed: {result2}")

    print("All test cases passed!")

if __name__ == "__main__":
    test_rob_iii()