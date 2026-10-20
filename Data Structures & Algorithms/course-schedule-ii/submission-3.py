class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        res = []
        graph = defaultdict(list)

        for cur, pre in prerequisites:
            graph[cur].append(pre)
        
        visited = set()
        cycle = set()
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
            if not dfs(i): return []
        return res
