class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderid = {c: i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            w1, w2 = words[i],words[i+1]

            for j in range(len(w1)):
                #w2已经完了，w1还有字符
                if j == len(w2):
                    return False
                
                #主要出现有一个不一样，并且次序较小，则不用比剩下的了
                if w1[j] != w2[j]:
                    if orderid[w1[j]] > orderid[w2[j]]:
                        return False
                    break
        
        return True
                
