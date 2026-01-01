"""
LeetCode 226: Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        """
        Recursive approach
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return

        # This works
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # This also works
        # root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)


        # This works
        tempLeft = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tempLeft)

        return root

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

# Helper function to convert tree to list (level order)
def tree_to_list(root):
    if not root:
        return []
    
    from collections import deque
    result = []
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
def test_invert_tree():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([4, 2, 7, 1, 3, 6, 9])
    inverted1 = solution.invertTree(root1)
    result1 = tree_to_list(inverted1)
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([2, 1, 3])
    inverted2 = solution.invertTree(root2)
    result2 = tree_to_list(inverted2)
    expected2 = [2, 3, 1]
    assert result2 == expected2, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Empty tree
    root3 = create_tree([])
    inverted3 = solution.invertTree(root3)
    result3 = tree_to_list(inverted3)
    assert result3 == [], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_invert_tree()

