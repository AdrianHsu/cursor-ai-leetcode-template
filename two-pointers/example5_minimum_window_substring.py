"""
LeetCode 76: Minimum Window Substring

Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
"""

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "" or len(s) < len(t):
            return ""

        def reachCount(need, have):
            for k, v in need.items():
                if have[k] < v:
                    return False
            return True
        
        need = defaultdict(int)

        for c in t:
            need[c] += 1
        
        have = defaultdict(int)
        min_window = ""

        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in need:
                have[c] += 1
            
            while reachCount(need, have):
                current_window = s[l:r+1]
                if min_window == "" or len(current_window) < len(min_window):
                    min_window = current_window
                have[s[l]] -= 1
                l += 1
            
        return min_window

# Test cases
def test_min_window():
    solution = Solution()
    
    # Test case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    result1 = solution.minWindow(s1, t1)
    assert result1 == "BANC", f"Test case 1 failed: got '{result1}', expected 'BANC'"
    print(f"Test case 1 passed: s='{s1}', t='{t1}' -> '{result1}'")
    
    # Test case 2
    s2 = "a"
    t2 = "a"
    result2 = solution.minWindow(s2, t2)
    assert result2 == "a", f"Test case 2 failed: got '{result2}', expected 'a'"
    print(f"Test case 2 passed: s='{s2}', t='{t2}' -> '{result2}'")
    
    # Test case 3
    s3 = "a"
    t3 = "aa"
    result3 = solution.minWindow(s3, t3)
    assert result3 == "", f"Test case 3 failed: got '{result3}', expected ''"
    print(f"Test case 3 passed: s='{s3}', t='{t3}' -> '{result3}'")
    
    # Test case 4
    s4 = "ab"
    t4 = "b"
    result4 = solution.minWindow(s4, t4)
    assert result4 == "b", f"Test case 4 failed: got '{result4}', expected 'b'"
    print(f"Test case 4 passed: s='{s4}', t='{t4}' -> '{result4}'")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_window()

