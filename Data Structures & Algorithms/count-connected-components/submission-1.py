class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for prev, cur in edges:
            graph[prev].append(cur)
            graph[cur].append(prev)
        

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res
            


