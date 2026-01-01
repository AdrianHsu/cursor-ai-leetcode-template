"""
LeetCode 547: Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

from collections import deque

class Solution:
    
    def findCircleNum(self, isConnected):
    #     """
    #     BFS approach
    #     Time Complexity: O(n^2)
    #     Space Complexity: O(n)
    #     """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def bfs(start):
            queue = deque([start])
            visited[start] = True

            while queue:
                city = queue.popleft()
                for neighbor in range(n):
                    if isConnected[city][neighbor] and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                bfs(i)
        
        return provinces

# Test cases
def test_find_circle_num():
    solution = Solution()
    
    # Test case 1
    isConnected1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result1 = solution.findCircleNum(isConnected1)
    assert result1 == 2, f"Test case 1 failed: got {result1}, expected 2"
    print(f"Test case 1 passed: {result1} provinces")
    
    # Test case 2
    isConnected2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result2 = solution.findCircleNum(isConnected2)
    assert result2 == 3, f"Test case 2 failed: got {result2}, expected 3"
    print(f"Test case 2 passed: {result2} provinces")
    
    # Test case 3: All connected
    isConnected3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    result3 = solution.findCircleNum(isConnected3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {result3} province")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_circle_num()

