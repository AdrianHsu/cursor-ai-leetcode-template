"""
LeetCode 42: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

i = 0: [0]
i = 1: [0, 1]
i = 2: [0, 1, 2]
i = 3: [0, 3] --> pop 2, pop 1
i = 4: [0, 3, 4]
i = 5: [] --> pop 4, pop 3, pop 0
"""

class Solution:

    def trap(self, height):
        # """
        # Monotonic stack approach
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # """
        stack = []
        water = 0

        for i, right_height in enumerate(height):
            while stack and height[stack[-1]] < right_height:
                target_index = stack.pop()
                target_height = height[target_index]
                if not stack:
                    break
                
                width = i - stack[-1] - 1
                # either left or right height (both taller than target_height)
                left_height = height[stack[-1]]
                trapped_height = min(left_height, right_height) - target_height
                water += width * trapped_height
            
            stack.append(i)

        return water


# Test cases
def test_trap():
    solution = Solution()
    
    # Test case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = solution.trap(height1)
    assert result1 == 6, f"Test case 1 failed: got {result1}, expected 6"
    print(f"Test case 1 passed: {height1} -> water = {result1}")
    
    # Test case 2
    height2 = [4, 2, 0, 3, 2, 5]
    result2 = solution.trap(height2)
    assert result2 == 9, f"Test case 2 failed: got {result2}, expected 9"
    print(f"Test case 2 passed: {height2} -> water = {result2}")
    
    # Test case 3
    height3 = [0, 1, 0, 2]
    result3 = solution.trap(height3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {height3} -> water = {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_trap()

