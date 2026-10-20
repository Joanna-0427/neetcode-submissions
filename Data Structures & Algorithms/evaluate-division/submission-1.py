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
            
            #seen不会陷入无限循环，因为是无向图有环parent；
            seen.add(a) #不用remove，因为找到了就退出，不会下个路径继续搜索；
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


