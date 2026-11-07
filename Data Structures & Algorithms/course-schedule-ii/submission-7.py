class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for cur, prev in prerequisites:
            graph[cur].append(prev)
        
        visited = set()
        cycle = set()
        res = []
        def dfs(node):
            if node in cycle:
                return False
            
            if node in visited:
                return True
            
            cycle.add(node)
            for ni in graph[node]:
                if not dfs(ni):return False

            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):return []
        
        return res
