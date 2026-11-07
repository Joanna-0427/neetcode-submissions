class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for cur,prev in prerequisites:
            graph[cur].append(prev)
        
        visited = set()
        def dfs(node):
            if not graph[node]:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)
            for ni in graph[node]:
                if not dfs(ni):return False
            
            graph[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):return False
        
        return True
            
            


