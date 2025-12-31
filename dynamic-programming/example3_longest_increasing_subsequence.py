"""
LeetCode 300: Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,18], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        Dynamic Programming - Bottom Up
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  # dp[i] = length of LIS ending at index i
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# Test cases
def test_length_of_lis():
    solution = Solution()
    
    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    result1 = solution.lengthOfLIS(nums1)
    assert result1 == 4, f"Test case 1 failed: got {result1}, expected 4"
    print(f"Test case 1 passed: {nums1} -> LIS length = {result1}")
    
    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    result2 = solution.lengthOfLIS(nums2)
    assert result2 == 4, f"Test case 2 failed: got {result2}, expected 4"
    print(f"Test case 2 passed: {nums2} -> LIS length = {result2}")
    
    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    result3 = solution.lengthOfLIS(nums3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {nums3} -> LIS length = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_lis()

