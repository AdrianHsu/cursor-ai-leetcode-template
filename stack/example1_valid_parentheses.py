"""
LeetCode 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s):
        """
        Stack-based solution
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                # Opening bracket
                stack.append(char)
        
        return not stack

# Test cases
def test_valid_parentheses():
    solution = Solution()
    
    # Test case 1
    s1 = "()"
    result1 = solution.isValid(s1)
    assert result1 == True, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: '{s1}' -> {result1}")
    
    # Test case 2
    s2 = "()[]{}"
    result2 = solution.isValid(s2)
    assert result2 == True, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: '{s2}' -> {result2}")
    
    # Test case 3
    s3 = "(]"
    result3 = solution.isValid(s3)
    assert result3 == False, f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: '{s3}' -> {result3}")
    
    # Test case 4
    s4 = "([)]"
    result4 = solution.isValid(s4)
    assert result4 == False, f"Test case 4 failed: got {result4}"
    print(f"Test case 4 passed: '{s4}' -> {result4}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_valid_parentheses()

