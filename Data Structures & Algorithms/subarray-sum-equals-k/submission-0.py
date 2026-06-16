class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0] = 1
        sum = 0
        res = 0
        for n in nums:
            sum += n
            target = sum - k
            if target in dic:
                res += dic[target]
        
            dic[sum] = dic.get(sum,0) + 1
        return res
            



        

        