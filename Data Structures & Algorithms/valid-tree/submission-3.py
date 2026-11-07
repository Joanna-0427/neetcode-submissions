class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return

            visited.add(node)
            for ni in graph[node]:
                if ni == parent:
                    continue
                dfs(ni,node)
        
        dfs(0,None)
        return len(visited) == n

            