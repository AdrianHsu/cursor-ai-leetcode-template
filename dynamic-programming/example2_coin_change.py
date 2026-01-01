"""
LeetCode 322: Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        Dynamic Programming - Bottom Up
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        # dp[i] means the minimum coins needed for amount i
        # eg., dp[10] means min number of coins needed for amount = 10
        
        dp = [float('inf') for i in range(amount + 1)]

        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                # dp[i - coin] is defined
                if i - coin >= 0:
                    
                    # [1,2,8,3,7]
                    # dp[10] = 3 (2,8 and 3,7 and 1,2,7) Why?
                    
                    # dp[3] = 2 (1,2 and 3)
                    # do[2] = 1, dp[1] = 1
                    # goes back to dp[0] = 0 
                    # so the equation needs a base, 1
                    # hence, (dp[i - coin] + 1)
                    

                    base = 1

                    dp[i] = min((dp[i - coin] +  base), dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
def test_coin_change():
    solution = Solution()
    
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = solution.coinChange(coins1, amount1)
    assert result1 == 3, f"Test case 1 failed: got {result1}, expected 3"
    print(f"Test case 1 passed: coins={coins1}, amount={amount1} -> {result1} coins")
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    result2 = solution.coinChange(coins2, amount2)
    assert result2 == -1, f"Test case 2 failed: got {result2}, expected -1"
    print(f"Test case 2 passed: coins={coins2}, amount={amount2} -> {result2}")
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    result3 = solution.coinChange(coins3, amount3)
    assert result3 == 0, f"Test case 3 failed: got {result3}, expected 0"
    print(f"Test case 3 passed: coins={coins3}, amount={amount3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_coin_change()

