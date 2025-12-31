"""
LeetCode 21: Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        return dummy.next

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
def test_merge_two_lists():
    solution = Solution()
    
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4], "Test case 1 failed"
    print("Test case 1 passed: [1,2,4] + [1,3,4] -> [1,1,2,3,4,4]")
    
    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [], "Test case 2 failed"
    print("Test case 2 passed: [] + [] -> []")
    
    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [0], "Test case 3 failed"
    print("Test case 3 passed: [] + [0] -> [0]")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_two_lists()

