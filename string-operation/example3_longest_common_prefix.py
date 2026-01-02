"""
LeetCode 14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# Test cases
def test_longest_common_prefix():
    solution = Solution()
    
    # Test case 1
    strs1 = ["flower", "flow", "flight"]
    result1 = solution.longestCommonPrefix(strs1)
    assert result1 == "fl", f"Test case 1 failed: got '{result1}'"
    print(f"Test case 1 passed: {strs1} -> '{result1}'")
    
    # Test case 2
    strs2 = ["dog", "racecar", "car"]
    result2 = solution.longestCommonPrefix(strs2)
    assert result2 == "", f"Test case 2 failed: got '{result2}'"
    print(f"Test case 2 passed: {strs2} -> '{result2}'")
    
    # Test case 3
    strs3 = ["ab", "a"]
    result3 = solution.longestCommonPrefix(strs3)
    assert result3 == "a", f"Test case 3 failed: got '{result3}'"
    print(f"Test case 3 passed: {strs3} -> '{result3}'")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_common_prefix()

