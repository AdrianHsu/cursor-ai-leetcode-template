"""
LeetCode 35: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        Binary search for insert position
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        l = 0 
        r= len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        # When the loop breaks, l is the insertion point
        return l

# Test cases
def test_search_insert():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3, 5, 6]
    target1 = 5
    result1 = solution.searchInsert(nums1, target1)
    assert result1 == 2, f"Test case 1 failed: got {result1}, expected 2"
    print(f"Test case 1 passed: {nums1}, target={target1} -> index {result1}")
    
    # Test case 2
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = solution.searchInsert(nums2, target2)
    assert result2 == 1, f"Test case 2 failed: got {result2}, expected 1"
    print(f"Test case 2 passed: {nums2}, target={target2} -> index {result2}")
    
    # Test case 3
    nums3 = [1, 3, 5, 6]
    target3 = 7
    result3 = solution.searchInsert(nums3, target3)
    assert result3 == 4, f"Test case 3 failed: got {result3}, expected 4"
    print(f"Test case 3 passed: {nums3}, target={target3} -> index {result3}")
    
    # Test case 4
    nums4 = [1, 3, 5, 6]
    target4 = 0
    result4 = solution.searchInsert(nums4, target4)
    assert result4 == 0, f"Test case 4 failed: got {result4}, expected 0"
    print(f"Test case 4 passed: {nums4}, target={target4} -> index {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_search_insert()

