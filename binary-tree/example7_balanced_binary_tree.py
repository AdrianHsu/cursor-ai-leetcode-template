"""
LeetCode 110: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        """
        Recursive approach: check height and balance at each node
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # If any subtree is unbalanced, return -1
            if left_height == -1 or right_height == -1:
                return -1
            
            # If height difference > 1, tree is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return get_height(root) != -1


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
def test_balanced_tree():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.isBalanced(root1)
    assert result1 == True, f"Test case 1 failed: got {result1}, expected True"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    result2 = solution.isBalanced(root2)
    assert result2 == False, f"Test case 2 failed: got {result2}, expected False"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Empty tree
    root3 = create_tree([])
    result3 = solution.isBalanced(root3)
    assert result3 == True, f"Test case 3 failed: got {result3}, expected True"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_balanced_tree()

