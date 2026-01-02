"""
LeetCode 125: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
"""

class Solution:
    
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True

# Test cases
def test_valid_palindrome():
    solution = Solution()
    
    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    result1 = solution.isPalindrome(s1)
    assert result1 == True, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: '{s1}' -> {result1}")
    
    # Test case 2
    s2 = "race a car"
    result2 = solution.isPalindrome(s2)
    assert result2 == False, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: '{s2}' -> {result2}")
    
    # Test case 3
    s3 = " "
    result3 = solution.isPalindrome(s3)
    assert result3 == True, f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: '{s3}' -> {result3}")
    
    # Test case 4
    s4 = "ab_a"
    result4 = solution.isPalindrome(s4)
    assert result4 == True, f"Test case 4 failed: got {result4}"
    print(f"Test case 4 passed: '{s4}' -> {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_valid_palindrome()

