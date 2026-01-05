"""
LeetCode 424: Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English letter. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s, k):
        """
        Sliding window with frequency counting
        Time Complexity: O(n)
        Space Complexity: O(1) - at most 26 characters
        """
        char_count = defaultdict(int)
        left = 0
        max_count = 0
        max_length = 0
        
        for right in range(len(s)):
            # Expand window
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])
            
            # Shrink window if we need more than k replacements
            # Window size - max_count = number of characters to replace
            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length


# Test cases
def test_character_replacement():
    solution = Solution()
    
    # Test case 1
    s1 = "ABAB"
    k1 = 2
    result1 = solution.characterReplacement(s1, k1)
    assert result1 == 4, f"Test case 1 failed: got {result1}, expected 4"
    print(f"Test case 1 passed: s='{s1}', k={k1} -> {result1}")
    
    # Test case 2
    s2 = "AABABBA"
    k2 = 1
    result2 = solution.characterReplacement(s2, k2)
    assert result2 == 4, f"Test case 2 failed: got {result2}, expected 4"
    print(f"Test case 2 passed: s='{s2}', k={k2} -> {result2}")
    
    # Test case 3
    s3 = "AAAA"
    k3 = 2
    result3 = solution.characterReplacement(s3, k3)
    assert result3 == 4, f"Test case 3 failed: got {result3}, expected 4"
    print(f"Test case 3 passed: s='{s3}', k={k3} -> {result3}")
    
    # Test case 4
    s4 = "ABAA"
    k4 = 0
    result4 = solution.characterReplacement(s4, k4)
    assert result4 == 2, f"Test case 4 failed: got {result4}, expected 2"
    print(f"Test case 4 passed: s='{s4}', k={k4} -> {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_character_replacement()

