"""
LeetCode 236: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        DFS approach: find p and q, return LCA
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        """
        if not root:
            return None
        
        # If root is one of the target nodes, return it
        if root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both found in different subtrees, root is LCA
        if left and right:
            return root
        
        # Return the non-None result (if one is found)
        return left or right


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

# Helper function to find node by value
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

# Test cases
def test_lowest_common_ancestor():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1 = find_node(root1, 5)
    q1 = find_node(root1, 1)
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    assert result1.val == 3, f"Test case 1 failed: got {result1.val if result1 else None}, expected 3"
    print(f"Test case 1 passed: LCA = {result1.val}")
    
    # Test case 2
    root2 = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p2 = find_node(root2, 5)
    q2 = find_node(root2, 4)
    result2 = solution.lowestCommonAncestor(root2, p2, q2)
    assert result2.val == 5, f"Test case 2 failed: got {result2.val if result2 else None}, expected 5"
    print(f"Test case 2 passed: LCA = {result2.val}")
    
    # Test case 3
    root3 = create_tree([1, 2])
    p3 = find_node(root3, 1)
    q3 = find_node(root3, 2)
    result3 = solution.lowestCommonAncestor(root3, p3, q3)
    assert result3.val == 1, f"Test case 3 failed: got {result3.val if result3 else None}, expected 1"
    print(f"Test case 3 passed: LCA = {result3.val}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_lowest_common_ancestor()

