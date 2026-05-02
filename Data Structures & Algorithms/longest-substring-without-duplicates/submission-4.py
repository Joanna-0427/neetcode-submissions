class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sset = set()
        longest = 0
        for right in range(len(s)):
            while s[right] in sset:
                sset.remove(s[left])
                left += 1
            length = right - left + 1
            longest = max(longest, length)
            sset.add(s[right])
            
        return longest

            



        