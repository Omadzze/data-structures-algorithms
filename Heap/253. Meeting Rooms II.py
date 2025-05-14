#https://leetcode.com/problems/meeting-rooms-ii/submissions/1633593418/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        """
        To understand how much rooms company would need it's required to sort time by start time,
        once we sorted we then can take up end time and push this to the min-heap.

        Once it's in min-heap we could check elements and pop from the min-heap and check whether
        meeting was ended or not. If meeting was ended it will simply use this room,
        else we need to increase counter++
        """


        free_rooms = []
        meeting_time = []

        for meeting in intervals:
            meeting_time.append(meeting)

        # sort meeting time
        meeting_time = sorted(meeting_time)

        # add first room to the first meeting
        heapq.heappush(free_rooms, meeting_time[0][1])

        # since first room was added we are starting from second
        for i in meeting_time[1:]:

            # assign room to the meeting if we have lag between end time and start tiem
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # otherwise we need to append new room
            heapq.heappush(free_rooms, i[1])

        # size of the heap is the minimum rooms that are required
        return len(free_rooms)