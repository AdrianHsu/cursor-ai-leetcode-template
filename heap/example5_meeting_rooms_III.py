"""
LeetCode 2402: Meeting Rooms III

You are given an integer n. There are n rooms numbered from 0 to n - 1.
You are given a 2D integer array meetings where meetings[i] = [start_i, end_i].
Meetings are allocated to rooms in the following way:
1. Each meeting will take place in the unused room with the lowest number.
2. If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
3. When a room becomes unused, meetings that have an earlier original start time should be given the room.

Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

Example 1:
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0

Example 2:
Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
"""

import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # """
        # Dual Heap Simulation approach
        # Time Complexity: O(M log M + M log N) where M is meetings, N is rooms
        # Space Complexity: O(N)
        # """
        
        # Sort by start time to process meetings in order
        meetings.sort()
        
        # Min-heap for available rooms (stores just room index)
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        
        # Min-heap for occupied rooms: stores (end_time, room_index)
        occupied_rooms = []
        
        # Track usage count for each room
        room_usage_count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have finished their meetings by the current start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)
            
            # If a room is available
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room))
            else:
                # No room available, we must delay the meeting
                # Pop the room that finishes earliest
                finish_time, room = heapq.heappop(occupied_rooms)
                
                # The new end time is the finish time of the previous meeting + duration of current
                duration = end - start
                new_end = finish_time + duration
                heapq.heappush(occupied_rooms, (new_end, room))
            
            room_usage_count[room] += 1
        
        # Find the room with max usage. Since index is tie-breaker and we iterate 0..n,
        # finding the first max is sufficient or using argmax logic.
        max_usage = -1
        result_room = -1
        
        for i in range(n):
            if room_usage_count[i] > max_usage:
                max_usage = room_usage_count[i]
                result_room = i
                
        return result_room

# Test cases
def test_most_booked():
    solution = Solution()
    
    # Test case 1
    n1 = 2
    meetings1 = [[0,10],[1,5],[2,7],[3,4]]
    result1 = solution.mostBooked(n1, meetings1)
    assert result1 == 0, f"Test case 1 failed: got {result1}, expected 0"
    print(f"Test case 1 passed: Room {result1}")
    
    # Test case 2
    n2 = 3
    meetings2 = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    result2 = solution.mostBooked(n2, meetings2)
    assert result2 == 1, f"Test case 2 failed: got {result2}, expected 1"
    print(f"Test case 2 passed: Room {result2}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_most_booked()