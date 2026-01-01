"""
LeetCode 26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        Two pointers: slow and fast
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1


# Test cases
def test_remove_duplicates():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 2, f"Test case 1 failed: got k={k1}"
    assert nums1[:k1] == [1, 2], f"Test case 1 failed: got {nums1[:k1]}"
    print(f"Test case 1 passed: k={k1}, nums={nums1[:k1]}")
    
    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 5, f"Test case 2 failed: got k={k2}"
    assert nums2[:k2] == [0, 1, 2, 3, 4], f"Test case 2 failed: got {nums2[:k2]}"
    print(f"Test case 2 passed: k={k2}, nums={nums2[:k2]}")
    
    # Test case 3: Single element
    nums3 = [1]
    k3 = solution.removeDuplicates(nums3)
    assert k3 == 1, f"Test case 3 failed: got k={k3}"
    assert nums3[:k3] == [1], f"Test case 3 failed: got {nums3[:k3]}"
    print(f"Test case 3 passed: k={k3}, nums={nums3[:k3]}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_remove_duplicates()

