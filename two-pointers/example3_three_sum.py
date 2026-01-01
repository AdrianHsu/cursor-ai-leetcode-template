"""
LeetCode 15: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums):
        """
        Sort + Two pointers
        Time Complexity: O(n^2)
        Space Complexity: O(1) excluding output
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result


# Test cases
def test_three_sum():
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    # Sort each triplet and the result for comparison
    result1 = [sorted(triplet) for triplet in result1]
    result1.sort()
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    expected1 = [sorted(triplet) for triplet in expected1]
    expected1.sort()
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {nums1} -> {result1}")
    
    # Test case 2
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    assert result2 == [], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {nums2} -> {result2}")
    
    # Test case 3
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    assert result3 == [[0, 0, 0]], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {nums3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_three_sum()

