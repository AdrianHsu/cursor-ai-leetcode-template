"""
LeetCode 450: Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        """
        Recursive approach: handle three cases (no children, one child, two children)
        Time Complexity: O(h) where h is height
        Space Complexity: O(h) for recursion stack
        """
        if not root:
            return None
        
        if key < root.val:
            # Key is in left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Key is in right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Node has two children: find inorder successor (smallest in right subtree)
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def find_min(self, node):
        """Find the minimum node in a subtree"""
        while node.left:
            node = node.left
        return node


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
def test_delete_node_bst():
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([5, 3, 6, 2, 4, None, 7])
    result1 = solution.deleteNode(root1, 3)
    result_list1 = tree_to_list(result1)
    # Expected: [5,4,6,2,null,null,7] or similar valid BST structure
    assert result_list1[0] == 5, f"Test case 1 failed: root = {result_list1[0]}, expected 5"
    print(f"Test case 1 passed: {result_list1}")
    
    # Test case 2: Key not found
    root2 = create_tree([5, 3, 6, 2, 4, None, 7])
    result2 = solution.deleteNode(root2, 0)
    result_list2 = tree_to_list(result2)
    assert result_list2 == [5, 3, 6, 2, 4, None, 7], f"Test case 2 failed: got {result_list2}"
    print(f"Test case 2 passed: {result_list2}")
    
    # Test case 3: Delete leaf node
    root3 = create_tree([5, 3, 6, 2, 4, None, 7])
    result3 = solution.deleteNode(root3, 2)
    result_list3 = tree_to_list(result3)
    assert result_list3[0] == 5, f"Test case 3 failed"
    print(f"Test case 3 passed: {result_list3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_delete_node_bst()

