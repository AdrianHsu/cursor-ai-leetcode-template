"""
LeetCode 46: Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

class Solution:
    def permute(self, nums):
        """
        Backtracking approach
        Time Complexity: O(n! * n)
        Space Complexity: O(n)
        """
        result = []
        
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
        
        backtrack([])
        return result

# Test cases
def test_permutations():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3]
    result1 = solution.permute(nums1)
    # Sort for comparison
    result1 = [sorted(perm) for perm in result1]
    result1.sort()
    expected1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    expected1 = [sorted(perm) for perm in expected1]
    expected1.sort()
    assert len(result1) == len(expected1), f"Test case 1 failed: wrong count"
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {len(result1)} permutations")
    
    # Test case 2
    nums2 = [0, 1]
    result2 = solution.permute(nums2)
    result2 = [sorted(perm) for perm in result2]
    result2.sort()
    expected2 = [[0, 1], [1, 0]]
    expected2 = [sorted(perm) for perm in expected2]
    expected2.sort()
    assert result2 == expected2, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3
    nums3 = [1]
    result3 = solution.permute(nums3)
    assert result3 == [[1]], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_permutations()

