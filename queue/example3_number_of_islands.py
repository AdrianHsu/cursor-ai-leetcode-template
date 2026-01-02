"""
LeetCode 200: Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from collections import deque

class Solution:

    # BFS solution
    def numIslands(self, grid):
        """
        BFS approach using queue
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            grid[start_row][start_col] = '0'  # Mark as visited
            
            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (0 <= new_row < rows and 0 <= new_col < cols and 
                        grid[new_row][new_col] == '1'):
                        grid[new_row][new_col] = '0'  # Mark as visited
                        queue.append((new_row, new_col))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)
        
        return islands


    # I wrote a DFS solution
    # def numIslands(self, grid):

    #     islands = 0
    #     if len(grid) == 0 or len(grid[0]) == 0:
    #         return 0
    #     m = len(grid)
    #     n = len(grid[0])

    #     directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    #     def dfs(i, j):

    #         if grid[i][j] == "1":
    #             grid[i][j] = "0"
            
    #         for direction in directions:
    #             di = i + direction[0]
    #             dj = j + direction[1]

    #             if di >= 0 and di < m and dj >= 0 and dj < n:
    #                 if grid[di][dj] == "1":
    #                     dfs(di, dj)

    #         return 

    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == "1":
    #                 islands += 1
    #                 dfs(i, j)

    #     return islands

# Test cases
def test_num_islands():
    solution = Solution()
    
    # Test case 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result1 = solution.numIslands([row[:] for row in grid1])  # Copy grid
    assert result1 == 1, f"Test case 1 failed: got {result1}, expected 1"
    print(f"Test case 1 passed: {result1} island(s)")
    
    # Test case 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result2 = solution.numIslands([row[:] for row in grid2])  # Copy grid
    assert result2 == 3, f"Test case 2 failed: got {result2}, expected 3"
    print(f"Test case 2 passed: {result2} island(s)")
    
    # Test case 3: Single island
    grid3 = [["1"]]
    result3 = solution.numIslands([row[:] for row in grid3])
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {result3} island(s)")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_num_islands()

