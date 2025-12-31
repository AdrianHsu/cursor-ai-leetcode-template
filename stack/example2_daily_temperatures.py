"""
LeetCode 739: Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        Monotonic stack approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        result = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        
        return result

# Test cases
def test_daily_temperatures():
    solution = Solution()
    
    # Test case 1
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = solution.dailyTemperatures(temps1)
    assert result1 == [1, 1, 4, 2, 1, 1, 0, 0], f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {temps1} -> {result1}")
    
    # Test case 2
    temps2 = [30, 40, 50, 60]
    result2 = solution.dailyTemperatures(temps2)
    assert result2 == [1, 1, 1, 0], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {temps2} -> {result2}")
    
    # Test case 3
    temps3 = [30, 60, 90]
    result3 = solution.dailyTemperatures(temps3)
    assert result3 == [1, 1, 0], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {temps3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_daily_temperatures()

