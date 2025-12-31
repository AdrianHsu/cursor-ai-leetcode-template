"""
LeetCode 150: Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation.
Evaluate the expression and return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
"""

class Solution:
    def evalRPN(self, tokens):
        """
        Stack-based evaluation
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # division
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]

# Test cases
def test_eval_rpn():
    solution = Solution()
    
    # Test case 1
    tokens1 = ["2", "1", "+", "3", "*"]
    result1 = solution.evalRPN(tokens1)
    assert result1 == 9, f"Test case 1 failed: got {result1}, expected 9"
    print(f"Test case 1 passed: {tokens1} -> {result1}")
    
    # Test case 2
    tokens2 = ["4", "13", "5", "/", "+"]
    result2 = solution.evalRPN(tokens2)
    assert result2 == 6, f"Test case 2 failed: got {result2}, expected 6"
    print(f"Test case 2 passed: {tokens2} -> {result2}")
    
    # Test case 3
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result3 = solution.evalRPN(tokens3)
    assert result3 == 22, f"Test case 3 failed: got {result3}, expected 22"
    print(f"Test case 3 passed: {tokens3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_eval_rpn()

