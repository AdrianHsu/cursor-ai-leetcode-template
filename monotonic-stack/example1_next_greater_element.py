"""
LeetCode 496: Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        Monotonic stack approach
        Time Complexity: O(n + m)
        Space Complexity: O(n)
        """
        stack = []
        next_greater = {}
        
        # Build next greater map for nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Find next greater for each element in nums1
        result = [next_greater.get(num, -1) for num in nums1]
        return result

# Test cases
def test_next_greater_element():
    solution = Solution()
    
    # Test case 1
    nums1_1 = [4, 1, 2]
    nums2_1 = [1, 3, 4, 2]
    result1 = solution.nextGreaterElement(nums1_1, nums2_1)
    assert result1 == [-1, 3, -1], f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: nums1={nums1_1}, nums2={nums2_1} -> {result1}")
    
    # Test case 2
    nums1_2 = [2, 4]
    nums2_2 = [1, 2, 3, 4]
    result2 = solution.nextGreaterElement(nums1_2, nums2_2)
    assert result2 == [3, -1], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: nums1={nums1_2}, nums2={nums2_2} -> {result2}")
    
    # Test case 3
    nums1_3 = [1]
    nums2_3 = [1, 2]
    result3 = solution.nextGreaterElement(nums1_3, nums2_3)
    assert result3 == [2], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: nums1={nums1_3}, nums2={nums2_3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_next_greater_element()

