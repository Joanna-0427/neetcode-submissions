class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],x[1]))
        res = 0
        prevend = intervals[0][1]
        for s, t in intervals[1:]:
            if s < prevend:
                res += 1
                prevend = min(t,prevend)
            else:
                prevend = t
        
        return res

