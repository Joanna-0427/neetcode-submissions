class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited: #有环检查
                return

            visited.add(node)
            for ni in graph[node]:
                if ni in visited:
                    continue
                dfs(ni)
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            else:
                count += 1
                dfs(i)
        
        return count
            

        