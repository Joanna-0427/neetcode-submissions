"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:(x.start,x.end))
        minheap = []
        rooms = 0
        i = 0
        
        while i < n:
            start, end = intervals[i].start, intervals[i].end
            if minheap and minheap[0] <= start:
                end = heapq.heappop(minheap)

            heapq.heappush(minheap,intervals[i].end)
            rooms = max(rooms,len(minheap))

            i += 1

        return rooms



