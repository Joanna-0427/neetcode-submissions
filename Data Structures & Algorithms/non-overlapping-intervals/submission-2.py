class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],x[1]))
        prevstart = intervals[0][0]
        prevend = intervals[0][1]
        remove = 0
        for start, end in intervals[1:]:
            if start < prevend:
                remove += 1
                prevend = min(prevend,end)
            else:
                prevend = end
        
        return remove

