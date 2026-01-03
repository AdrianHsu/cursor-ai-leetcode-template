"""
LeetCode 252: Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""

class Solution:
    def canAttendMeetings(self, intervals):
        # """
        # Sorting approach
        # Time Complexity: O(n log n) due to sorting
        # Space Complexity: O(1) (excluding input storage)
        # """
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            # If the current meeting starts before the previous one ends, there is an overlap
            if intervals[i][0] < intervals[i-1][1]:
                return False
                
        return True

# Test cases
def test_can_attend_meetings():
    solution = Solution()
    
    # Test case 1: Overlapping meetings
    intervals1 = [[0,30],[5,10],[15,20]]
    result1 = solution.canAttendMeetings(intervals1)
    assert result1 == False, f"Test case 1 failed: got {result1}, expected False"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2: Non-overlapping meetings
    intervals2 = [[7,10],[2,4]]
    result2 = solution.canAttendMeetings(intervals2)
    assert result2 == True, f"Test case 2 failed: got {result2}, expected True"
    print(f"Test case 2 passed: {result2}")
    
    # Test case 3: Empty input
    intervals3 = []
    result3 = solution.canAttendMeetings(intervals3)
    assert result3 == True, f"Test case 3 failed: got {result3}, expected True"
    print(f"Test case 3 passed: {result3}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_can_attend_meetings()