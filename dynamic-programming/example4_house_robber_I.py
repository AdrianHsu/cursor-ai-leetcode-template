"""
LeetCode 198: House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
"""

class Solution:
    def rob(self, nums):
        # """
        # Dynamic Programming approach (Space Optimized)
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # """
        if not nums:
            return 0
        
        # prev1 represents dp[i-1], prev2 represents dp[i-2]
        prev1, prev2 = 0, 0
        
        for num in nums:
            # Current max is either:
            # 1. Robbing current house + loot from i-2 (num + prev2)
            # 2. Skipping current house and keeping loot from i-1 (prev1)
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
            
        return prev1

# Test cases
def test_rob():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1]
    result1 = solution.rob(nums1)
    assert result1 == 4, f"Test case 1 failed: got {result1}, expected 4"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    result2 = solution.rob(nums2)
    assert result2 == 12, f"Test case 2 failed: got {result2}, expected 12"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Single house
    nums3 = [5]
    result3 = solution.rob(nums3)
    assert result3 == 5, f"Test case 3 failed: got {result3}, expected 5"
    print(f"Test case 3 passed: {result3}")

    print("All test cases passed!")

if __name__ == "__main__":
    test_rob()