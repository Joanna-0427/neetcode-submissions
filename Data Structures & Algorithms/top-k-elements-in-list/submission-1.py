class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)

        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0) + 1
        for key, value in dic.items():
            res[value].append(key)

        ans = []
        for freq in range(len(nums),0,-1):
            if freq in res:
                for num in res[freq]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
                        



