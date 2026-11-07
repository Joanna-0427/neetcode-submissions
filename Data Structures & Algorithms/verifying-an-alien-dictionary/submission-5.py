class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for i, k in enumerate(order):
            mapping[k] = i
        n = len(words)
        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            i = j = 0
            if w1.startswith(w2):return False
            if w2.startswith(w1):return True
            while i < len(w1) and j < len(w2):
                if mapping[w1[i]] > mapping[w2[j]]:
                    return False
                elif mapping[w1[i]] < mapping[w2[j]]:
                    break
                else:
                    i += 1
                    j += 1
            
        
        return True

            
