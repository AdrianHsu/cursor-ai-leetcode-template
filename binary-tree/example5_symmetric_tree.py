"""
LeetCode 101: Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        """
        Recursive approach: check if left and right subtrees are mirrors
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return True
        
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    is_mirror(left.left, right.right) and 
                    is_mirror(left.right, right.left))
        
        return is_mirror(root.left, root.right)


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
def test_symmetric_tree():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([1, 2, 2, 3, 4, 4, 3])
    result1 = solution.isSymmetric(root1)
    assert result1 == True, f"Test case 1 failed: got {result1}, expected True"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([1, 2, 2, None, 3, None, 3])
    result2 = solution.isSymmetric(root2)
    assert result2 == False, f"Test case 2 failed: got {result2}, expected False"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Single node
    root3 = create_tree([1])
    result3 = solution.isSymmetric(root3)
    assert result3 == True, f"Test case 3 failed: got {result3}, expected True"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_symmetric_tree()

