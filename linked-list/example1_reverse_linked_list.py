"""
LeetCode 206: Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_reverse_linked_list():
    solution = Solution()
    
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseList(head1)
    assert linked_list_to_list(result1) == [5, 4, 3, 2, 1], "Test case 1 failed"
    print("Test case 1 passed: [1,2,3,4,5] -> [5,4,3,2,1]")
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    result2 = solution.reverseList(head2)
    assert linked_list_to_list(result2) == [2, 1], "Test case 2 failed"
    print("Test case 2 passed: [1,2] -> [2,1]")
    
    # Test case 3
    head3 = create_linked_list([])
    result3 = solution.reverseList(head3)
    assert linked_list_to_list(result3) == [], "Test case 3 failed"
    print("Test case 3 passed: [] -> []")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_linked_list()

