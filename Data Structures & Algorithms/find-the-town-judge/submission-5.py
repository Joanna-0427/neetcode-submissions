class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = defaultdict(int)
        income = defaultdict(int)

        for k, v in trust:
            out[k] += 1
            income[v] += 1
        
        for i in range(n+1):
            #judge收到的trust=n-1，并且给出去的trust是0
            if income[i] == n-1 and i not in out:
                return i
        
        return -1
