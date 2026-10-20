class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #无环
        edge = len(edges)
        if edge != n-1:
            return False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        #连通
        visited = set()
        def dfs(node):
            visited.add(node)
            for ni in graph[node]:
                if ni not in visited:
                    dfs(ni)
        
        dfs(0)
        return len(visited) == n
