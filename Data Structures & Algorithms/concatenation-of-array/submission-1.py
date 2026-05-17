class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans

        # ans = []
        # for i in range(2):
        #     for i in nums:
        #         ans.append(i)
        # return ans