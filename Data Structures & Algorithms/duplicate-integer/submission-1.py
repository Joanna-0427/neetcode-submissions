class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         return True
        #     dic[i] = 1
        # return False
        


        newnum = set(nums)
        if len(nums) - len(newnum) > 0:
            return True
        return False

