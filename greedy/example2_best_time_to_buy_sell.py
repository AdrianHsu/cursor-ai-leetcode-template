"""
LeetCode 121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices):
        """
        Greedy approach: track minimum price and maximum profit
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit

# Test cases
def test_max_profit():
    solution = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(prices1)
    assert result1 == 5, f"Test case 1 failed: got {result1}, expected 5"
    print(f"Test case 1 passed: {prices1} -> profit = {result1}")
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(prices2)
    assert result2 == 0, f"Test case 2 failed: got {result2}, expected 0"
    print(f"Test case 2 passed: {prices2} -> profit = {result2}")
    
    # Test case 3
    prices3 = [1, 2]
    result3 = solution.maxProfit(prices3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {prices3} -> profit = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_profit()

