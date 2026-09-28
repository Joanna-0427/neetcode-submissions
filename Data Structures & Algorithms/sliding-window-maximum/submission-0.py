class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []

        for j in range(n):

            #新元素来了和最近加入q[-1]的比较(q[0]存的是当前窗口的最大值)
            while q and nums[q[-1]] < nums[j]:
                q.pop()

            q.append(j)

            #q[0]只有读取答案+判断过期才维护
            if q[0] < j-k+1:
                q.popleft()
            
            #只需要j满足，窗口形成k以后每一轮一定满足。
            if j+1 >= k:
                res.append(nums[q[0]])
        
        return res
