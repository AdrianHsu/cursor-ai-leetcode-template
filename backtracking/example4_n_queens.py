"""
LeetCode 51: N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

Example 2:
Input: n = 1
Output: [["Q"]]
"""

class Solution:
    def __init__(self):
        self.results = []

    def solveNQueens(self, n):
        self.results = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        def isSafe(row, col):

            # Case 1: same column does not have a queen
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Case 2: same row does not have a queen
            # Always True because we choose where to put Q on a row

            # Case 3: diagonal `\`
            di = row - 1
            dj = col - 1
            while di >= 0 and dj >= 0:
                if board[di][dj] == 'Q':
                    return False
                di -= 1
                dj -= 1
 
            # Case 4: diagonal `/`
            di = row - 1
            dj = col + 1
            while di >= 0 and dj < n:
                if board[di][dj] == 'Q':
                    return False
                di -= 1
                dj += 1                       

            return True

        
        def backtrack(row):
            if row == n:
                # Convert board to list of strings
                solution = [''.join(row) for row in board]
                self.results.append(solution[:])
                return
            
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'  # Make choice
                    backtrack(row + 1)      # Recurse
                    board[row][col] = '.'   # Undo choice
        
        backtrack(0)
        return self.results

# Test cases
def test_n_queens():
    solution = Solution()
    
    # Test case 1
    n1 = 4
    result1 = solution.solveNQueens(n1)
    expected1 = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    # Sort for comparison
    result1.sort()
    expected1.sort()
    assert len(result1) == len(expected1), f"Test case 1 failed: wrong count, got {len(result1)}, expected {len(expected1)}"
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: n={n1} -> {len(result1)} solutions")
    
    # Test case 2
    n2 = 1
    result2 = solution.solveNQueens(n2)
    assert result2 == [["Q"]], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: n={n2} -> {result2}")
    
    # Test case 3
    n3 = 2
    result3 = solution.solveNQueens(n3)
    assert result3 == [], f"Test case 3 failed: got {result3}, expected []"
    print(f"Test case 3 passed: n={n3} -> {len(result3)} solutions (no solution exists)")
    
    # Test case 4
    n4 = 3
    result4 = solution.solveNQueens(n4)
    assert result4 == [], f"Test case 4 failed: got {result4}, expected []"
    print(f"Test case 4 passed: n={n4} -> {len(result4)} solutions (no solution exists)")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_n_queens()

