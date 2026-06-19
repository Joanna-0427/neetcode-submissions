class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setnum = set(nums) #[5,4,3,20,2] need to put in set before
        for n in nums:
            if n-1 not in setnum:
                length = 1
                while n + length in setnum:
                    length += 1
                longest = max(longest,length)
    
        return longest
            

            
            
            

            
