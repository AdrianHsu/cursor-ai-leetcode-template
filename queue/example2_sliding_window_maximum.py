"""
LeetCode 239: Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Monotonic deque approach
        Time Complexity: O(n)
        Space Complexity: O(k)
        """
        queue = deque()
        result = []
        
        for i, num in enumerate(nums):
            # Remove indices outside current window
            while queue and queue[0] <= i - k:
                queue.popleft()
            
            # Remove indices with smaller values
            while queue and nums[queue[-1]] < num:
                queue.pop()
            
            queue.append(i)
            
            # Add to result when window is complete
            if i >= k - 1:
                result.append(nums[queue[0]])
        
        return result

# Test cases
def test_sliding_window_maximum():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    result1 = solution.maxSlidingWindow(nums1, k1)
    assert result1 == [3, 3, 5, 5, 6, 7], f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {nums1}, k={k1} -> {result1}")
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    result2 = solution.maxSlidingWindow(nums2, k2)
    assert result2 == [1], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {nums2}, k={k2} -> {result2}")
    
    # Test case 3
    nums3 = [1, -1]
    k3 = 1
    result3 = solution.maxSlidingWindow(nums3, k3)
    assert result3 == [1, -1], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {nums3}, k={k3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_sliding_window_maximum()

