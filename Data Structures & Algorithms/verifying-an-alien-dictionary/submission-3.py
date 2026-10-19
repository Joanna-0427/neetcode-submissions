class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {k:i for i,k in enumerate(order)}

        n = len(words)
        for i in range(n-1):
            w1, w2 = words[i],words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order[w1[j]] > order[w2[j]]:
                        return False
                    break
        
        return True

