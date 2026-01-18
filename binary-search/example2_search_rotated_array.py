"""
LeetCode 33: Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

class Solution:
    def search(self, nums, target):
        """
        Binary search in rotated sorted array
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            # Check if nums[m] is target
            if nums[m] == target:
                return m

            # when nums[m] is not target
            # Check which side is sorted.
            if nums[l] <= nums[m]: # Left is sorted, Right is not
                if nums[l] <= target < nums[m]: # healthy side. check it is in-bound
                    r = m - 1
                else: # messy side: it can be because target >= nums[m]  OR target (0) < nums[l] (4)
                    l = m + 1
            else: # nums[l] > nums[m]. Right is sorted, Left is not
                if nums[m] < target <= nums[r]: # healthy side. check it is in-bound
                    l = m + 1
                else: 
                    r = m - 1
        return -1

# Test cases
def test_search_rotated():
    solution = Solution()
    
    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = solution.search(nums1, target1)
    assert result1 == 4, f"Test case 1 failed: got {result1}, expected 4"
    print(f"Test case 1 passed: {nums1}, target={target1} -> index {result1}")
    
    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = solution.search(nums2, target2)
    assert result2 == -1, f"Test case 2 failed: got {result2}, expected -1"
    print(f"Test case 2 passed: {nums2}, target={target2} -> {result2}")
    
    # Test case 3
    nums3 = [1]
    target3 = 0
    result3 = solution.search(nums3, target3)
    assert result3 == -1, f"Test case 3 failed: got {result3}, expected -1"
    print(f"Test case 3 passed: {nums3}, target={target3} -> {result3}")
    
    # Test case 4
    nums4 = [5, 1, 3]
    target4 = 3
    result4 = solution.search(nums4, target4)
    assert result4 == 2, f"Test case 4 failed: got {result4}, expected 2"
    print(f"Test case 4 passed: {nums4}, target={target4} -> index {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_search_rotated()

