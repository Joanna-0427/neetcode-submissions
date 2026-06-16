class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        longest = 0
        l = 0
        new_count = {}
        need = len(count)

        have = 0
        resLen = float('inf')
        res = ''
        for r in range(len(s)):
            if s[r] not in count:
                continue
            new_count[s[r]] = new_count.get(s[r],0) + 1
            if new_count[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                while s[l] not in count:
                    l += 1
                    
                if r - l + 1 < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                if s[l] in count:
                    new_count[s[l]] -= 1
                    if new_count[s[l]] < count[s[l]]:
                        have -= 1
                    
                l += 1
        
        return res if resLen != float('inf') else ''

            


            
                
