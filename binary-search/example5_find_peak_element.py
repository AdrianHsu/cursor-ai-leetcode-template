"""
LeetCode 162: Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

class Solution:
    def findPeakElement(self, nums):
        """
        Binary search to find peak element
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        l = 0
        r = len(nums) - 1

        # [1,2,3,4,5,2,3]
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m 
        return l


# Test cases
def test_find_peak():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1]
    result1 = solution.findPeakElement(nums1)
    assert result1 == 2, f"Test case 1 failed: got {result1}, expected 2"
    print(f"Test case 1 passed: {nums1} -> peak at index {result1}")
    
    # Test case 2
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    result2 = solution.findPeakElement(nums2)
    assert result2 in [1, 5], f"Test case 2 failed: got {result2}, expected 1 or 5"
    print(f"Test case 2 passed: {nums2} -> peak at index {result2}")
    
    # Test case 3
    nums3 = [1]
    result3 = solution.findPeakElement(nums3)
    assert result3 == 0, f"Test case 3 failed: got {result3}, expected 0"
    print(f"Test case 3 passed: {nums3} -> peak at index {result3}")
    
    # Test case 4
    nums4 = [1, 2]
    result4 = solution.findPeakElement(nums4)
    assert result4 == 1, f"Test case 4 failed: got {result4}, expected 1"
    print(f"Test case 4 passed: {nums4} -> peak at index {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_peak()

