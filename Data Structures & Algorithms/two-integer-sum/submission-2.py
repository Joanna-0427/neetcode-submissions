class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dic to store element that haven't been matched
        # go through the list, if can found in the dic, then get results, if not, store in the dic

        dic = {}
        for i, n in enumerate(nums):
            if (target - n) in dic:
                return [dic[target - n],i]
            else:
                dic[n] = i

