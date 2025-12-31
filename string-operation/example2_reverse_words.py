"""
LeetCode 151: Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution:
    def reverseWords(self, s):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Split by whitespace and filter out empty strings
        words = s.split()
        # Reverse and join
        return ' '.join(reversed(words))

# Test cases
def test_reverse_words():
    solution = Solution()
    
    # Test case 1
    s1 = "the sky is blue"
    result1 = solution.reverseWords(s1)
    assert result1 == "blue is sky the", f"Test case 1 failed: got '{result1}'"
    print(f"Test case 1 passed: '{s1}' -> '{result1}'")
    
    # Test case 2
    s2 = "  hello world  "
    result2 = solution.reverseWords(s2)
    assert result2 == "world hello", f"Test case 2 failed: got '{result2}'"
    print(f"Test case 2 passed: '{s2}' -> '{result2}'")
    
    # Test case 3
    s3 = "a good   example"
    result3 = solution.reverseWords(s3)
    assert result3 == "example good a", f"Test case 3 failed: got '{result3}'"
    print(f"Test case 3 passed: '{s3}' -> '{result3}'")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_words()

