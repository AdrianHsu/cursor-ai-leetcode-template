"""
LeetCode 322: Coin Change (Greedy Pattern - works for canonical systems only)

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Note: This greedy approach works for "canonical coin systems" (like US coins: 1, 5, 10, 25, 50, 100) but does NOT work for all coin systems. For arbitrary coin systems, use Dynamic Programming (see DP examples).

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1 (3 coins)

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount 3 cannot be made up with coins of value 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for amount 0.

Note: For canonical coin systems (like US coins [1,5,10,25]), greedy works. 
For non-canonical systems (e.g., [1,3,4] with amount=6), greedy fails - use DP instead.
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        LeetCode 322: For canonical coin systems, greedy works.
        For arbitrary systems, use DP (see dynamic-programming examples).
        
        Greedy approach: always use the largest coin possible
        Time Complexity: O(n) where n is number of coin types
        Space Complexity: O(1)
        
        Warning: This greedy approach only works for canonical coin systems!
        For arbitrary coin systems, use dynamic programming instead.
        """
        if amount == 0:
            return 0
        
        # Sort coins in descending order
        coins.sort(reverse=True)
        
        count = 0
        remaining = amount
        
        for coin in coins:
            if remaining >= coin:
                num_coins = remaining // coin
                count += num_coins
                remaining %= coin
                
                if remaining == 0:
                    break
        
        # If we couldn't make exact change, return -1
        return count if remaining == 0 else -1

# Test cases
def test_coin_change():
    solution = Solution()
    
    # Test case 1: LeetCode example
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = solution.coinChange(coins1, amount1)
    expected1 = 3  # 5 + 5 + 1
    assert result1 == expected1, f"Test case 1 failed: got {result1}, expected {expected1}"
    print(f"Test case 1 passed: amount={amount1} -> {result1} coins")
    
    # Test case 2: LeetCode example
    coins2 = [2]
    amount2 = 3
    result2 = solution.coinChange(coins2, amount2)
    expected2 = -1
    assert result2 == expected2, f"Test case 2 failed: got {result2}, expected {expected2}"
    print(f"Test case 2 passed: amount={amount2} -> {result2} (cannot make change)")
    
    # Test case 3: LeetCode example
    coins3 = [1]
    amount3 = 0
    result3 = solution.coinChange(coins3, amount3)
    expected3 = 0
    assert result3 == expected3, f"Test case 3 failed: got {result3}, expected {expected3}"
    print(f"Test case 3 passed: amount={amount3} -> {result3} coins")
    
    # Test case 4: US coin system (canonical - greedy works)
    coins4 = [1, 5, 10, 25]
    amount4 = 67
    result4 = solution.coinChange(coins4, amount4)
    expected4 = 6  # 25*2 + 10*1 + 5*1 + 1*2
    assert result4 == expected4, f"Test case 4 failed: got {result4}, expected {expected4}"
    print(f"Test case 4 passed: amount={amount4} -> {result4} coins")
    
    # Test case 5: Another canonical system
    coins5 = [1, 5, 10, 25]
    amount5 = 30
    result5 = solution.coinChange(coins5, amount5)
    expected5 = 2  # 25 + 5
    assert result5 == expected5, f"Test case 5 failed: got {result5}, expected {expected5}"
    print(f"Test case 5 passed: amount={amount5} -> {result5} coins")
    
    print("All test cases passed!")
    print("\nNote: Greedy works for canonical coin systems (like US coins).")
    print("For non-canonical systems (e.g., [1, 3, 4] with amount=6), use Dynamic Programming instead.")

if __name__ == "__main__":
    test_coin_change()

