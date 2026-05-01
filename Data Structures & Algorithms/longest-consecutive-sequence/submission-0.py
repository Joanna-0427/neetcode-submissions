class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0
        for i in nums:
            if i - 1 not in new_nums:
                length = 1
                cur = i
                while cur + 1 in new_nums:
                    length += 1
                    cur += 1
                longest = max(longest,length)
        return longest

            

            
            
            

            
