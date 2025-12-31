"""
LeetCode 55: Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps from index 1 to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, nums):
        """
        Greedy approach: track maximum reachable position
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_reach = 0
        
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= len(nums) - 1:
                return True
        
        return True

# Test cases
def test_jump_game():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.canJump(nums1)
    assert result1 == True, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {nums1} -> {result1}")
    
    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.canJump(nums2)
    assert result2 == False, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {nums2} -> {result2}")
    
    # Test case 3: Single element
    nums3 = [0]
    result3 = solution.canJump(nums3)
    assert result3 == True, f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {nums3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_jump_game()

