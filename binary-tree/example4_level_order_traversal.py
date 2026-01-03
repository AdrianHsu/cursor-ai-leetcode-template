"""
LeetCode 102: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

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

from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        BFS approach using queue
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result


# Helper function to create tree from list
def create_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
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
def test_level_order():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.levelOrder(root1)
    assert result1 == [[3], [9, 20], [15, 7]], f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([1])
    result2 = solution.levelOrder(root2)
    assert result2 == [[1]], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3
    root3 = create_tree([])
    result3 = solution.levelOrder(root3)
    assert result3 == [], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_level_order()

