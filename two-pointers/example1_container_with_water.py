"""
LeetCode 11: Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height):
        """
        Two pointers from opposite ends
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        l = 0
        r = len(height) - 1
        max_water = 0

        while l < r:
            width = r - l
            current_area = width * min(height[l], height[r])
            max_water = max(max_water, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water


# Test cases
def test_max_area():
    solution = Solution()
    
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution.maxArea(height1)
    assert result1 == 49, f"Test case 1 failed: got {result1}, expected 49"
    print(f"Test case 1 passed: {height1} -> {result1}")
    
    # Test case 2
    height2 = [1, 1]
    result2 = solution.maxArea(height2)
    assert result2 == 1, f"Test case 2 failed: got {result2}, expected 1"
    print(f"Test case 2 passed: {height2} -> {result2}")
    
    # Test case 3
    height3 = [1, 2, 1]
    result3 = solution.maxArea(height3)
    assert result3 == 2, f"Test case 3 failed: got {result3}, expected 2"
    print(f"Test case 3 passed: {height3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_area()

