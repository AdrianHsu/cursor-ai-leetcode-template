"""
LeetCode 108: Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        """
        Recursive approach: use middle element as root
        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack
        """
        if not nums:
            return None
        
        # Find middle index
        mid = len(nums) // 2
        
        # Create root from middle element
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root


# Helper function to convert tree to list (level order)
def tree_to_list(root):
    if not root:
        return []
    
    result = []
    from collections import deque
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
def test_sorted_array_to_bst():
    solution = Solution()
    
    # Test case 1
    nums1 = [-10, -3, 0, 5, 9]
    root1 = solution.sortedArrayToBST(nums1)
    # Check if it's a valid BST by checking inorder traversal
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    result1 = inorder(root1)
    assert result1 == nums1, f"Test case 1 failed: inorder = {result1}, expected {nums1}"
    print(f"Test case 1 passed: inorder = {result1}")
    
    # Test case 2
    nums2 = [1, 3]
    root2 = solution.sortedArrayToBST(nums2)
    result2 = inorder(root2)
    assert result2 == nums2, f"Test case 2 failed: inorder = {result2}, expected {nums2}"
    print(f"Test case 2 passed: inorder = {result2}")
    
    # Test case 3: Single element
    nums3 = [1]
    root3 = solution.sortedArrayToBST(nums3)
    result3 = inorder(root3)
    assert result3 == nums3, f"Test case 3 failed: inorder = {result3}, expected {nums3}"
    print(f"Test case 3 passed: inorder = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_sorted_array_to_bst()

