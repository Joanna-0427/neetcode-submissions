"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        cnt = 0
        minheap = []
        n = len(intervals)
        i = 0
        while i < n:
            s, e = intervals[i].start,intervals[i].end
            while minheap and minheap[0] <= s:
                heapq.heappop(minheap)
            
            heapq.heappush(minheap,e)
            cnt = max(cnt,len(minheap))
            i += 1
        
        return cnt
            




            