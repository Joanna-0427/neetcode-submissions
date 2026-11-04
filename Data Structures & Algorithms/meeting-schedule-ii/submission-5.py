"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for i in intervals:
            events.append((i.start,1)) #append要(())
            events.append((i.end,-1))
        
        events.sort(key = lambda x:(x[0],x[1]))
        count = 0
        res = 0
        for e in events:
            if e[1] == 1:
                count += 1
            else:
                count -= 1
            res = max(res,count)
        return res
            
        