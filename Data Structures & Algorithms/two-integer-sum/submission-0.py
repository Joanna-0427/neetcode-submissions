class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in dic:
                return sorted([i,dic[ans]])
            dic[nums[i]] = i
