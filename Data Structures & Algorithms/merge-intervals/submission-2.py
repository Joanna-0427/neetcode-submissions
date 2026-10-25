class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for i in range(1,n):
            s, e = intervals[i]
            if s <= end:
                end = max(e,end)
            else:
                res.append([start,end])
                start = s
                end = e
        res.append([start,end])
        return res

