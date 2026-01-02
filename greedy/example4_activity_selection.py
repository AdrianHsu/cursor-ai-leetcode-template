"""
LeetCode 435: Non-overlapping Intervals (Activity Selection Pattern)

Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: This problem uses the same greedy pattern as the classic Activity Selection Problem - sort by end time and greedily select non-overlapping intervals.

Classic Activity Selection: Select maximum number of non-overlapping activities.
This LeetCode problem: Remove minimum intervals to make the rest non-overlapping (inverse problem, same greedy approach).

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note: This demonstrates the Activity Selection greedy pattern - sort by end time and always keep the interval that ends earliest.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        LeetCode 435: Greedy approach using Activity Selection pattern
        Sort by end time, always keep the interval that ends earliest
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1)
        """
        if not intervals:
            return 0
        
        # Sort by end time (finishing time)
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            # If this interval overlaps with the last kept interval, remove it
            if start < last_end:
                count += 1
            else:
                # Keep this interval, update last_end
                last_end = end
        
        return count
    
    def activity_selection(self, activities):
        """
        Classic Activity Selection: Select maximum non-overlapping activities
        Same greedy approach - sort by end time, always pick the activity that ends earliest
        """
        if not activities:
            return []
        
        # Sort by end time (finishing time)
        activities.sort(key=lambda x: x[1])
        
        result = [activities[0]]
        last_end = activities[0][1]
        
        for start, end in activities[1:]:
            # If this activity starts after the last one ended, we can do it
            if start >= last_end:
                result.append((start, end))
                last_end = end
        
        return result

# Test cases
def test_erase_overlap_intervals():
    solution = Solution()
    
    # Test case 1: LeetCode example
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result1 = solution.eraseOverlapIntervals(intervals1)
    expected1 = 1
    assert result1 == expected1, f"Test case 1 failed: got {result1}, expected {expected1}"
    print(f"Test case 1 passed: {intervals1} -> remove {result1} intervals")
    
    # Test case 2: LeetCode example
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    result2 = solution.eraseOverlapIntervals(intervals2)
    expected2 = 2
    assert result2 == expected2, f"Test case 2 failed: got {result2}, expected {expected2}"
    print(f"Test case 2 passed: {intervals2} -> remove {result2} intervals")
    
    # Test case 3: LeetCode example
    intervals3 = [[1, 2], [2, 3]]
    result3 = solution.eraseOverlapIntervals(intervals3)
    expected3 = 0
    assert result3 == expected3, f"Test case 3 failed: got {result3}, expected {expected3}"
    print(f"Test case 3 passed: {intervals3} -> remove {result3} intervals")
    
    # Test case 4: Classic activity selection (for reference)
    activities4 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    result4 = solution.activity_selection(activities4)
    expected4 = [(1, 4), (5, 7), (8, 11), (12, 14)]
    assert result4 == expected4, f"Test case 4 failed: got {result4}, expected {expected4}"
    print(f"Test case 4 passed: {len(result4)} activities selected (classic problem)")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_erase_overlap_intervals()

