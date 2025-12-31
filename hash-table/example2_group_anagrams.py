"""
LeetCode 49: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        Time Complexity: O(n * k log k) where n is number of strings, k is max length
        Space Complexity: O(n * k)
        """
        groups = defaultdict(list)
        
        for s in strs:
            # Use sorted string as key
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())

# Test cases
def test_group_anagrams():
    solution = Solution()
    
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.groupAnagrams(strs1)
    # Sort each group and the result for comparison
    result1 = [sorted(group) for group in result1]
    result1.sort()
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected1 = [sorted(group) for group in expected1]
    expected1.sort()
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {strs1} -> {result1}")
    
    # Test case 2
    strs2 = [""]
    result2 = solution.groupAnagrams(strs2)
    assert result2 == [[""]], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {strs2} -> {result2}")
    
    # Test case 3
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    assert result3 == [["a"]], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {strs3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams()

