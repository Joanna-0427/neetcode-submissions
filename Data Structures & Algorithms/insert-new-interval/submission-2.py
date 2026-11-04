class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        [[1,2],[4,6],[7,10]] [11,12]
        """
        n = len(intervals)
        res = []
        for i in range(n):
            if newInterval[0] > intervals[i][1]: #[1,2]    [11,12]
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]: #[9,10] [6,7]
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:                                 #有重叠区间 [4,7] [5,8]不立即append，先把newInterval更新后再和下一个比较
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
        res.append(newInterval)
        return res