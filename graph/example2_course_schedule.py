"""
LeetCode 207: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        Topological sort using Kahn's algorithm
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        # Build graph and in-degree
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Find all courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0
        
        while queue:
            course = queue.popleft()
            completed += 1
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return completed == numCourses

# Test cases
def test_course_schedule():
    solution = Solution()
    
    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    result1 = solution.canFinish(numCourses1, prerequisites1)
    assert result1 == True, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: numCourses={numCourses1}, prerequisites={prerequisites1} -> {result1}")
    
    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    result2 = solution.canFinish(numCourses2, prerequisites2)
    assert result2 == False, f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: numCourses={numCourses2}, prerequisites={prerequisites2} -> {result2}")
    
    # Test case 3
    numCourses3 = 3
    prerequisites3 = [[1, 0], [2, 1]]
    result3 = solution.canFinish(numCourses3, prerequisites3)
    assert result3 == True, f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: numCourses={numCourses3}, prerequisites={prerequisites3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_course_schedule()

