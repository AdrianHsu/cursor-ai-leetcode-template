"""
LeetCode 213: House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
"""

class Solution:
    def rob(self, nums):
        # """
        # DP approach reusing logic from House Robber I
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Helper function to solve the linear version (House Robber I)
        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for money in houses:
                temp = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = temp
            return prev1

        # Since houses are circular, we can't rob both the first and the last.
        # Scenario 1: Rob houses 0 to n-2 (exclude last house)
        # Scenario 2: Rob houses 1 to n-1 (exclude first house)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Test cases
def test_rob_ii():
    solution = Solution()
    
    # Test case 1: Circular constraint prevents taking first and last
    nums1 = [2, 3, 2]
    result1 = solution.rob(nums1)
    assert result1 == 3, f"Test case 1 failed: got {result1}, expected 3"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    nums2 = [1, 2, 3, 1]
    result2 = solution.rob(nums2)
    assert result2 == 4, f"Test case 2 failed: got {result2}, expected 4"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Smallest circle
    nums3 = [1, 2] # Can only rob max(1, 2)
    result3 = solution.rob(nums3)
    assert result3 == 2, f"Test case 3 failed: got {result3}, expected 2"
    print(f"Test case 3 passed: {result3}")

    print("All test cases passed!")

if __name__ == "__main__":
    test_rob_ii()