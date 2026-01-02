"""
LeetCode 34: Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        """
        Find first and last position using binary search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        def find_leftmost(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def find_rightmost(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1
        
        left_pos = find_leftmost(nums, target)
        
        if left_pos == len(nums) or nums[left_pos] != target:
            return [-1, -1]
        
        right_pos = find_rightmost(nums, target)
        return [left_pos, right_pos]


# Test cases
def test_search_range():
    solution = Solution()
    
    # Test case 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    result1 = solution.searchRange(nums1, target1)
    assert result1 == [3, 4], f"Test case 1 failed: got {result1}, expected [3, 4]"
    print(f"Test case 1 passed: {nums1}, target={target1} -> {result1}")
    
    # Test case 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    result2 = solution.searchRange(nums2, target2)
    assert result2 == [-1, -1], f"Test case 2 failed: got {result2}, expected [-1, -1]"
    print(f"Test case 2 passed: {nums2}, target={target2} -> {result2}")
    
    # Test case 3
    nums3 = []
    target3 = 0
    result3 = solution.searchRange(nums3, target3)
    assert result3 == [-1, -1], f"Test case 3 failed: got {result3}, expected [-1, -1]"
    print(f"Test case 3 passed: {nums3}, target={target3} -> {result3}")
    
    # Test case 4
    nums4 = [1]
    target4 = 1
    result4 = solution.searchRange(nums4, target4)
    assert result4 == [0, 0], f"Test case 4 failed: got {result4}, expected [0, 0]"
    print(f"Test case 4 passed: {nums4}, target={target4} -> {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_search_range()

