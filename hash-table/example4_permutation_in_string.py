"""
LeetCode 567: Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Example 3:
Input: s1 = "abc", s2 = "bbbca"
Output: true
Explanation: s2 contains "bca" which is a permutation of "abc".

Note: This demonstrates the sliding window with hash pattern - use frequency counting to track characters in the window.
"""

class Solution:
    def checkInclusion(self, s1, s2):
        """
        Sliding window with hash map to count character frequencies
        Time Complexity: O(n) where n is length of s2
        Space Complexity: O(1) - at most 26 characters
        """
        if len(s1) > len(s2):
            return False
        
        # Count frequency of characters in s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        # Sliding window in s2
        window_count = {}
        left = 0
        
        for right in range(len(s2)):
            # Expand window: add character at right
            char_right = s2[right]
            window_count[char_right] = window_count.get(char_right, 0) + 1
            
            # Shrink window if it's larger than s1's length
            while right - left + 1 > len(s1):
                char_left = s2[left]
                window_count[char_left] -= 1
                if window_count[char_left] == 0:
                    del window_count[char_left]
                left += 1
            
            # Check if current window is a permutation of s1
            if window_count == s1_count:
                return True
        
        return False

# Test cases
def test_check_inclusion():
    solution = Solution()
    
    # Test case 1: LeetCode example
    s1_1 = "ab"
    s2_1 = "eidbaooo"
    result1 = solution.checkInclusion(s1_1, s2_1)
    assert result1 == True, f"Test case 1 failed: got {result1}, expected True"
    print(f"Test case 1 passed: s1='{s1_1}', s2='{s2_1}' -> {result1}")
    
    # Test case 2: LeetCode example
    s1_2 = "ab"
    s2_2 = "eidboaoo"
    result2 = solution.checkInclusion(s1_2, s2_2)
    assert result2 == False, f"Test case 2 failed: got {result2}, expected False"
    print(f"Test case 2 passed: s1='{s1_2}', s2='{s2_2}' -> {result2}")
    
    # Test case 3: LeetCode example
    s1_3 = "abc"
    s2_3 = "bbbca"
    result3 = solution.checkInclusion(s1_3, s2_3)
    assert result3 == True, f"Test case 3 failed: got {result3}, expected True"
    print(f"Test case 3 passed: s1='{s1_3}', s2='{s2_3}' -> {result3}")
    
    # Test case 4: s1 longer than s2
    s1_4 = "abcd"
    s2_4 = "abc"
    result4 = solution.checkInclusion(s1_4, s2_4)
    assert result4 == False, f"Test case 4 failed: got {result4}, expected False"
    print(f"Test case 4 passed: s1='{s1_4}', s2='{s2_4}' -> {result4}")
    
    # Test case 5: Permutation at the start
    s1_5 = "adc"
    s2_5 = "dcda"
    result5 = solution.checkInclusion(s1_5, s2_5)
    assert result5 == True, f"Test case 5 failed: got {result5}, expected True"
    print(f"Test case 5 passed: s1='{s1_5}', s2='{s2_5}' -> {result5}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_check_inclusion()

