class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        count = Counter(t)
        need = len(count)

        have = 0
        window = {}
        i = 0
        distance = float('inf')
        res = ''

        #不管在不在，不能直接跳过，后面收缩窗口，还是要window[s[i]]-1；
        #s[j]在count里重置i=j，使得每一步的i都更新，丢失了最早的i信息；
        for j in range(n):
            
            #不管在不在都记录
            window[s[j]] =window.get(s[j],0) + 1

            if s[j] in count:       
                if window[s[j]] == count[s[j]]:
                    have += 1
            
            #检查状态是否合法
            while have == need:
                if j-i+1 < distance:
                    res = s[i:j+1]
                    distance = j-i+1
            
                window[s[i]] -= 1
                if window[s[i]] == count[s[i]] - 1:
                    have -= 1
                i += 1
        
        return res
        
                