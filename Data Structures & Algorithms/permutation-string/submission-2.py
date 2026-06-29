class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        need = len(count)

        window = {}
        have = 0
        l = 0
        for r in range(len(s2)):
            if s2[r] in count:
                window[s2[r]] = window.get(s2[r],0) + 1
                if window[s2[r]] == count[s2[r]]: #s2[r] must in count
                    have += 1
            
            while r - l + 1 > len(s1):
                if s2[l] in count:
                    if window[s2[l]] == count[s2[l]]:
                        have -= 1
                    window[s2[l]] -= 1
                l += 1

            if have == need:
                return True
            
        return False

