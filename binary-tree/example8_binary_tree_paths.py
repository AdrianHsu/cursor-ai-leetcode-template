"""
LeetCode 257: Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        """
        DFS approach with backtracking
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return []
        
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Add current node to path
            path.append(str(node.val))
            
            # If leaf node, add path to result
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                # Continue DFS
                dfs(node.left, path)
                dfs(node.right, path)
            
            # Backtrack: remove current node from path
            path.pop()
        
        dfs(root, [])
        return result


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
def test_binary_tree_paths():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([1, 2, 3, None, 5])
    result1 = solution.binaryTreePaths(root1)
    expected1 = ["1->2->5", "1->3"]
    assert set(result1) == set(expected1), f"Test case 1 failed: got {result1}, expected {expected1}"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    root2 = create_tree([1])
    result2 = solution.binaryTreePaths(root2)
    assert result2 == ["1"], f"Test case 2 failed: got {result2}, expected ['1']"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3
    root3 = create_tree([1, 2])
    result3 = solution.binaryTreePaths(root3)
    assert result3 == ["1->2"], f"Test case 3 failed: got {result3}, expected ['1->2']"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_binary_tree_paths()

