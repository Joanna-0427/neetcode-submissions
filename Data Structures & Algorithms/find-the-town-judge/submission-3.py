class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        visited = set()
        for i in range(len(trust)):
            visited.add(trust[i][0])

        if len(visited) != n-1:
            return -1
        
        for j in range(1,n+1):
            if j not in visited:
                judge = j
        
        times = 0
        for t in range(len(trust)):
            if trust[t][1] == judge:
                times += 1
        
        if times != n-1:
            return -1
        
        return judge