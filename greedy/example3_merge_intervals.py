"""
LeetCode 56: Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    def merge(self, intervals):
        """
        Greedy approach: sort and merge overlapping intervals
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            
            # If current overlaps with last, merge them
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        return merged

# Test cases
def test_merge_intervals():
    solution = Solution()
    
    # Test case 1
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = solution.merge(intervals1)
    assert result1 == [[1, 6], [8, 10], [15, 18]], f"Test case 1 failed: got {result1}"
    print(f"Test case 1 passed: {intervals1} -> {result1}")
    
    # Test case 2
    intervals2 = [[1, 4], [4, 5]]
    result2 = solution.merge(intervals2)
    assert result2 == [[1, 5]], f"Test case 2 failed: got {result2}"
    print(f"Test case 2 passed: {intervals2} -> {result2}")
    
    # Test case 3
    intervals3 = [[1, 4], [0, 4]]
    result3 = solution.merge(intervals3)
    assert result3 == [[0, 4]], f"Test case 3 failed: got {result3}"
    print(f"Test case 3 passed: {intervals3} -> {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_intervals()

