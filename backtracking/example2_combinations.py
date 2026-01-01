"""
LeetCode 77: Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
"""

class Solution:
    def __init__(self):
        self.results = []

    def combine(self, n, k):
        self.results = []

        def backtrack(start, curr):
            if len(curr) == k:
                self.results.append(curr[:])
                return

            for i in range(start, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])
        return self.results

# Test cases
def test_combinations():
    solution = Solution()
    
    # Test case 1
    n1, k1 = 4, 2
    result1 = solution.combine(n1, k1)
    result1.sort()
    expected1 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    expected1.sort()
    assert result1 == expected1, f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: n={n1}, k={k1} -> {len(result1)} combinations")
    
    # Test case 2
    n2, k2 = 1, 1
    result2 = solution.combine(n2, k2)
    assert result2 == [[1]], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: n={n2}, k={k2} -> {result2}")
    
    # Test case 3
    n3, k3 = 3, 2
    result3 = solution.combine(n3, k3)
    result3.sort()
    expected3 = [[1, 2], [1, 3], [2, 3]]
    expected3.sort()
    assert result3 == expected3, f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: n={n3}, k={k3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_combinations()

