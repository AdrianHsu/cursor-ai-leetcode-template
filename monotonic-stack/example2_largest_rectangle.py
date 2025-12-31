"""
LeetCode 84: Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the shaded area, which has area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""

class Solution:
    def largestRectangleArea(self, heights):
        """
        Monotonic stack approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        max_area = 0
        
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        # Process remaining bars
        while stack:
            h = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area

# Test cases
def test_largest_rectangle():
    solution = Solution()
    
    # Test case 1
    heights1 = [2, 1, 5, 6, 2, 3]
    result1 = solution.largestRectangleArea(heights1)
    assert result1 == 10, f"Test case 1 failed: got {result1}, expected 10"
    print(f"Test case 1 passed: {heights1} -> area = {result1}")
    
    # Test case 2
    heights2 = [2, 4]
    result2 = solution.largestRectangleArea(heights2)
    assert result2 == 4, f"Test case 2 failed: got {result2}, expected 4"
    print(f"Test case 2 passed: {heights2} -> area = {result2}")
    
    # Test case 3
    heights3 = [1]
    result3 = solution.largestRectangleArea(heights3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {heights3} -> area = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_rectangle()

