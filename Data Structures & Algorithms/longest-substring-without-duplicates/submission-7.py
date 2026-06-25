class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #left point -  right point = longest
        #if duplicate: move left until there is no duplicate, then update longest

        left = 0
        longest = 0
        setnum = set()
        
        
        for right in range(len(s)):
            while s[right] in setnum:
                setnum.remove(s[left])
                left += 1
            setnum.add(s[right])
            longest = max(right-left+1,longest)
        return longest




        