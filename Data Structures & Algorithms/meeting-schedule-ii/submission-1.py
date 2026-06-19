"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        minheap = []
        res = 0
        for n in intervals:
            start, end = n.start, n.end
            if minheap and start >= minheap[0][0]:
                heapq.heappop(minheap)
            else:
                res += 1
            heapq.heappush(minheap,(end,start))
        return res
            

