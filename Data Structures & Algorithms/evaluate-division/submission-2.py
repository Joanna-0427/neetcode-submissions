class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        graph = defaultdict(dict)
        for (de, num), val in zip(equations,values):
            graph[de][num] = val
            graph[num][de] = 1 / val
        
        visited = set()
        def dfs(a,b,visited):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            
            visited.add(a) #因为node含有parent，需要用visited排除无限循环
            for ni,val in graph[a].items():
                if ni in visited:
                    continue
                r = dfs(ni,b,visited)
                if r != -1.0:
                    return r*val
            return -1.0
        
        for de, nu in queries:
            res.append(dfs(de,nu,set()))
        
        return res
            
                

