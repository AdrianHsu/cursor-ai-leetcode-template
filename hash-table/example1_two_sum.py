"""
LeetCode 1: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums, target):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# Test cases
def test_two_sum():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert sorted(result1) == [0, 1], f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {nums1}, target={target1} -> {result1}")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert sorted(result2) == [1, 2], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {nums2}, target={target2} -> {result2}")
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert sorted(result3) == [0, 1], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {nums3}, target={target3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()

