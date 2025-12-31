"""
LeetCode 141: Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        """
        Floyd's Cycle Detection Algorithm (Tortoise and Hare)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

# Helper function to create linked list with cycle
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
    
    nodes = [ListNode(val) for val in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

# Test cases
def test_has_cycle():
    solution = Solution()
    
    # Test case 1: Cycle exists
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert solution.hasCycle(head1) == True, "Test case 1 failed"
    print("Test case 1 passed: Cycle detected in [3,2,0,-4]")
    
    # Test case 2: Cycle exists at head
    head2 = create_linked_list_with_cycle([1, 2], 0)
    assert solution.hasCycle(head2) == True, "Test case 2 failed"
    print("Test case 2 passed: Cycle detected in [1,2]")
    
    # Test case 3: No cycle
    head3 = create_linked_list_with_cycle([1], -1)
    assert solution.hasCycle(head3) == False, "Test case 3 failed"
    print("Test case 3 passed: No cycle in [1]")
    
    # Test case 4: Empty list
    assert solution.hasCycle(None) == False, "Test case 4 failed"
    print("Test case 4 passed: No cycle in empty list")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_has_cycle()

