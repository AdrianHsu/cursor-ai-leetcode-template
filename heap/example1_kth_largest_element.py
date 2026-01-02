"""
LeetCode 215: Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import heapq # heapq means heap queue

class Solution:
    def findKthLargest(self, nums, k):
        """
        Use min heap of size k
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # it is a min heap
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            # since heapq is a queue, so when pop() it pops the popleft() ie., the head
            # pop the minimal one, the head, ie., heap[0]
            if len(heap) > k:
                v = heapq.heappop(heap)
                print(v)
        
        # Since it is min-heap, so 
        # heap[0] is the head. ie., the smallest amongst these K items
        # heap[-1] is the tail, ie., the biggest amongst these K items
        # return the smallest one
        print("heap[-1]", heap[-1])
        print("heap[0]", heap[0])
        return heap[0]

    # def findKthLargest(self, nums, k):
    #     heap = []

    #     for num in nums:
    #         heapq.heappush(heap, num)
    #         if len(heap) > k:
    #             heapq.heappop(heap)
    #     return heap[0]



# Test cases
def test_kth_largest():
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = solution.findKthLargest(nums1, k1)
    assert result1 == 5, f"Test case 1 failed: got {result1}, expected 5"
    print(f"Test case 1 passed: {nums1}, k={k1} -> {result1}")
    
    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    assert result2 == 4, f"Test case 2 failed: got {result2}, expected 4"
    print(f"Test case 2 passed: {nums2}, k={k2} -> {result2}")
    
    # Test case 3
    nums3 = [1]
    k3 = 1
    result3 = solution.findKthLargest(nums3, k3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {nums3}, k={k3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_kth_largest()

