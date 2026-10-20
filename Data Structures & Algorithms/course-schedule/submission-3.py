class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for cur, prev in prerequisites:
            graph[cur].append(prev)
        
        memo = {}
        visited = set()
        def dfs(node):
            if node in memo:
                return memo[node]
 
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited: return False
                if not dfs(neighbor): return False
            
            visited.remove(node) #和add配对，谁加入谁移除
            
            memo[node] = True
            return True
        
        return all(dfs(i) for i in range(numCourses))



