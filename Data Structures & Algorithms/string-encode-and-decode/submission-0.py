class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i= 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            res.append(s[j+1:j+1+num])
            i = j + 1 + num
        return res


