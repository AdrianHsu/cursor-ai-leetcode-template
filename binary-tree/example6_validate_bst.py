"""
LeetCode 98: Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

The Trap! Consider a tree where the root is 5 and its right child is 8. This is valid. 
But if 8 has a left child 3, that 3 is less than 8 (locally correct), but it is also less than 5. 
Since it's in the right subtree of 5, it must be greater than 5.

Hence, we have to pass down (min, max) as a backtracking param
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        """
        DFS approach: track min and max bounds for each node
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if current node value is within bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))


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
def test_validate_bst():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([2, 1, 3])
    result1 = solution.isValidBST(root1)
    assert result1 == True, f"Test case 1 failed: got {result1}, expected True"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([5, 1, 4, None, None, 3, 6])
    result2 = solution.isValidBST(root2)
    assert result2 == False, f"Test case 2 failed: got {result2}, expected False"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Single node
    root3 = create_tree([1])
    result3 = solution.isValidBST(root3)
    assert result3 == True, f"Test case 3 failed: got {result3}, expected True"
    print(f"Test case 3 passed: {result3}")
    
    # Test case 4: Invalid BST
    root4 = create_tree([5, 4, 6, None, None, 3, 7])
    result4 = solution.isValidBST(root4)
    assert result4 == False, f"Test case 4 failed: got {result4}, expected False"
    print(f"Test case 4 passed: {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_validate_bst()

