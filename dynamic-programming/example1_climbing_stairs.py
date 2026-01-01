"""
LeetCode 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    # def climbStairs(self, n):
    #     """
    #     Dynamic Programming - Bottom Up
    #     Time Complexity: O(n)
    #     Space Complexity: O(1)
    #     """
    #     if n <= 2:
    #         return n
        
    #     prev2 = 1  # ways to reach step 0
    #     prev1 = 2  # ways to reach step 1
        
    #     for i in range(3, n + 1):
    #         current = prev1 + prev2
    #         prev2 = prev1
    #         prev1 = current
        
    #     return prev1

    def climbStairs(self, n):
        if n <= 2:
            return n
        
        dp = [0 for i in range(n + 1)]
        dp[0] = -1 # not used
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Test cases
def test_climb_stairs():
    solution = Solution()
    
    # Test case 1
    n1 = 2
    result1 = solution.climbStairs(n1)
    assert result1 == 2, f"Test case 1 failed: got {result1}, expected 2"
    print(f"Test case 1 passed: n={n1} -> {result1} ways")
    
    # Test case 2
    n2 = 3
    result2 = solution.climbStairs(n2)
    assert result2 == 3, f"Test case 2 failed: got {result2}, expected 3"
    print(f"Test case 2 passed: n={n2} -> {result2} ways")
    
    # Test case 3
    n3 = 5
    result3 = solution.climbStairs(n3)
    assert result3 == 8, f"Test case 3 failed: got {result3}, expected 8"
    print(f"Test case 3 passed: n={n3} -> {result3} ways")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_climb_stairs()

