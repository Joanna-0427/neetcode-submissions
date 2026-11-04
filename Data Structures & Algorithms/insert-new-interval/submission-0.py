class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n = len(intervals)
        merge = [intervals[0]]

        
        for start,end in intervals[1:]:
            last = merge[-1]
            if start <= last[1]:
                last[1] = max(end,last[1])
            else:
                merge.append([start,end])
        
        return merge
                