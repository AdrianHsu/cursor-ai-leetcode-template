"""
LeetCode 704: Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

class Solution:
    def search(self, nums, target):
        """
        Standard binary search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else: return m
        
        return -1


# Test cases
def test_binary_search():
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    result1 = solution.search(nums1, target1)
    assert result1 == 4, f"Test case 1 failed: got {result1}, expected 4"
    print(f"Test case 1 passed: {nums1}, target={target1} -> index {result1}")
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    result2 = solution.search(nums2, target2)
    assert result2 == -1, f"Test case 2 failed: got {result2}, expected -1"
    print(f"Test case 2 passed: {nums2}, target={target2} -> {result2}")
    
    # Test case 3
    nums3 = [5]
    target3 = 5
    result3 = solution.search(nums3, target3)
    assert result3 == 0, f"Test case 3 failed: got {result3}, expected 0"
    print(f"Test case 3 passed: {nums3}, target={target3} -> index {result3}")
    
    # Test case 4
    nums4 = [2, 5]
    target4 = 0
    result4 = solution.search(nums4, target4)
    assert result4 == -1, f"Test case 4 failed: got {result4}, expected -1"
    print(f"Test case 4 passed: {nums4}, target={target4} -> {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_binary_search()

