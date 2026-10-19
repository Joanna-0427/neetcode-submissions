class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        received_trust = defaultdict(int)
        give_trust = set()
        for i in range(len(trust)):
            give_trust.add(trust[i][0])
            received_trust[trust[i][1]] += 1
        
        judge = None
        for j in range(1,n+1):
            if j not in give_trust:
                judge = j
        
        if judge is None:
            return -1
        
        if received_trust[judge] == n-1:
            return judge
        return -1


        