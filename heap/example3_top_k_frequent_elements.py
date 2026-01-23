"""
LeetCode 347: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        Use min heap to keep top k frequent elements
        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """
        counterMap = defaultdict(int)
        for num in nums:
            counterMap[num] += 1
        
        heap = []
        for num, cnt in counterMap.items():
            heapq.heappush(heap, (-cnt, num))
        
        res = []
        for i in range(k):
            cnt_neg, num = heapq.heappop(heap)
            res.append(num)
        return res

# Test cases
def test_top_k_frequent():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    assert set(result1) == {1, 2}, f"Test case 1 failed: got {result1}, expected [1, 2]"
    print(f"Test case 1 passed: {nums1}, k={k1} -> {result1}")
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    assert result2 == [1], f"Test case 2 failed: got {result2}, expected [1]"
    print(f"Test case 2 passed: {nums2}, k={k2} -> {result2}")
    
    # Test case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    result3 = solution.topKFrequent(nums3, k3)
    assert set(result3) == {-1, 2}, f"Test case 3 failed: got {result3}, expected [-1, 2]"
    print(f"Test case 3 passed: {nums3}, k={k3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_top_k_frequent()

