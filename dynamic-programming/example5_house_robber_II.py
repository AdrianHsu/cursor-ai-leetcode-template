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

Hint: cannot rob both 0 or n - 1
Ie.,
you can only rob either 0 (and no n-1) or rob n - 1 (and no 0)
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
    
    # def rob(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     elif len(nums) == 1:
    #         return nums[0]
        
    #     n = len(nums)
    #     dp1 = [0] * len(nums)
    #     dp2 = [0] * len(nums)

    #     # Case 1: don't rob [0], and do rob [n - 1]
    #     dp1[0] = 0
    #     dp1[1] = nums[1]
    #     for i in range(2, n):
    #         dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

            
    #     # Case 2: do rob [0], and don't rob [n - 1]
    #     dp2[0] = nums[0]
    #     dp2[1] = max(nums[0], nums[1])
    #     dp2[n- 1] = 0
    #     for i in range(2, n - 1):
    #         dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

    #     # Case 3: don't rob both [0] and [n - 1]? doesnt make sense

    #     return max(dp1[n - 1], dp2[n - 2])

    # def rob(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
        
    #     def rob_simple(house_list):
    #         if not house_list: 
    #             return 0
            
    #         dp = [0] * len(house_list)
    #         dp[0] = house_list[0]
            
    #         if len(house_list) > 1:
    #             dp[1] = max(house_list[0], house_list[1])
            
    #         for i in range(2, len(house_list)):
    #             dp[i] = max(dp[i-1], dp[i-2] + house_list[i])
                
    #         return dp[-1]

    #     return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))

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