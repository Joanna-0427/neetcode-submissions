class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = {}
        # res = 0
        # max_count = 0
        # left = 0

        # for right in range(len(s)):
        #     count[s[right]] = count.get(s[right],0) + 1
        #     max_count = max(max_count,count[s[right]])

        #     while right - left + 1 - max_count > k:
        #         count[s[left]] -= 1
        #         left += 1
            
        #     res = max(res, right - left + 1)
        # return res

    
        window = {}
        maxlen = 0
        
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            
            if r - l + 1 - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
        
            maxlen = max(maxlen, r - l + 1)

        return maxlen















            


