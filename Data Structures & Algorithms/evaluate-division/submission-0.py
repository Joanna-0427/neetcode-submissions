class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x,y), val in zip(equations,values):
            graph[x][y] = val
            graph[y][x] = 1 / val
        
        def dfs(a,b,seen):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            
            seen.add(a)
            for nd, w in graph[a].items():
                if nd not in seen:
                    r = dfs(nd,b,seen)
                    if r != -1.0:
                        return w * r
            
            return -1.0
        
        res = []
        for c, d in queries:
            res.append(dfs(c,d,set()))
        return res


