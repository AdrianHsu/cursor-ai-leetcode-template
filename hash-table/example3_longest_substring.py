"""
LeetCode 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Sliding window with hash map
        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is charset size
        """
        char_index = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If character seen and within current window, move left pointer
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Test cases
def test_longest_substring():
    solution = Solution()
    
    # Test case 1
    s1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(s1)
    assert result1 == 3, f"Test case 1 failed: got {result1}, expected 3"
    print(f"Test case 1 passed: '{s1}' -> {result1}")
    
    # Test case 2
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    assert result2 == 1, f"Test case 2 failed: got {result2}, expected 1"
    print(f"Test case 2 passed: '{s2}' -> {result2}")
    
    # Test case 3
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    assert result3 == 3, f"Test case 3 failed: got {result3}, expected 3"
    print(f"Test case 3 passed: '{s3}' -> {result3}")
    
    # Test case 4: Empty string
    s4 = ""
    result4 = solution.lengthOfLongestSubstring(s4)
    assert result4 == 0, f"Test case 4 failed: got {result4}, expected 0"
    print(f"Test case 4 passed: '{s4}' -> {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_substring()

