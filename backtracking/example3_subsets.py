"""
LeetCode 78: Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums):
    #     """
    #     Backtracking approach
    #     Time Complexity: O(2^n * n)
    #     Space Complexity: O(n)
    #     """"
        result = []

        def backtrack(nums, i, curr):
            
            result.append(curr[:])

            for i in range(i, len(nums)):
                curr.append(nums[i])
                backtrack(nums, i + 1, curr)
                curr.pop()
            return

        backtrack(nums, 0, [])
        return result

# Test cases
def test_subsets():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3]
    result1 = solution.subsets(nums1)
    # Sort each subset and the result for comparison
    result1 = [sorted(subset) for subset in result1]
    result1.sort(key=len)
    result1.sort()
    expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    expected1 = [sorted(subset) for subset in expected1]
    expected1.sort(key=len)
    expected1.sort()
    assert len(result1) == len(expected1), f"Test case 1 failed: wrong count"
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {len(result1)} subsets")
    
    # Test case 2
    nums2 = [0]
    result2 = solution.subsets(nums2)
    result2 = [sorted(subset) for subset in result2]
    result2.sort()
    expected2 = [[], [0]]
    expected2 = [sorted(subset) for subset in expected2]
    expected2.sort()
    assert result2 == expected2, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {result2}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_subsets()

