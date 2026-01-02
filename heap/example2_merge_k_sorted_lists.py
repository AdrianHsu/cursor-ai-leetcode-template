"""
LeetCode 23: Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        Use min heap to merge k sorted lists
        Time Complexity: O(n log k) where n is total nodes, k is number of lists
        Space Complexity: O(k)
        """
        heap = []
        
        # Push first node of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            node_val, list_idx, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
            curr.next = node
            curr = curr.next
        
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
def test_merge_k_lists():
    solution = Solution()
    
    # Test case 1
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1 = solution.mergeKLists(lists1)
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    assert linked_list_to_list(result1) == expected1, f"Test case 1 failed"
    print(f"Test case 1 passed: merged lists -> {linked_list_to_list(result1)}")
    
    # Test case 2
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    assert result2 is None, f"Test case 2 failed"
    print(f"Test case 2 passed: empty lists -> None")
    
    # Test case 3
    lists3 = [create_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    assert result3 is None, f"Test case 3 failed"
    print(f"Test case 3 passed: [[]] -> None")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_k_lists()

