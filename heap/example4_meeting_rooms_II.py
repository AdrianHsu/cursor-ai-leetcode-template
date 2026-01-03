"""
LeetCode 253: Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        # """
        # Min-Heap approach
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        # """
        if not intervals:
            return 0
            
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min-heap to store the end times of active meetings
        free_rooms = []
        
        # Push the first meeting's end time
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            
            # If the room with the earliest end time is free by the time this meeting starts
            if free_rooms[0] <= current_start:
                heapq.heappop(free_rooms)
            
            # Add the current meeting's end time to the heap
            heapq.heappush(free_rooms, current_end)
            
        # The size of the heap tells us how many rooms are currently occupied at peak
        return len(free_rooms)

# Test cases
def test_min_meeting_rooms():
    solution = Solution()
    
    # Test case 1
    intervals1 = [[0,30],[5,10],[15,20]]
    result1 = solution.minMeetingRooms(intervals1)
    assert result1 == 2, f"Test case 1 failed: got {result1}, expected 2"
    print(f"Test case 1 passed: {result1} rooms")
    
    # Test case 2
    intervals2 = [[7,10],[2,4]]
    result2 = solution.minMeetingRooms(intervals2)
    assert result2 == 1, f"Test case 2 failed: got {result2}, expected 1"
    print(f"Test case 2 passed: {result2} room")

    # Test case 3: Consecutive meetings (should reuse room)
    intervals3 = [[1, 5], [5, 10], [10, 15]]
    result3 = solution.minMeetingRooms(intervals3)
    assert result3 == 1, f"Test case 3 failed: got {result3}, expected 1"
    print(f"Test case 3 passed: {result3} room")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_meeting_rooms()