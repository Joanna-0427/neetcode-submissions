class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(numCourses)}
        for prev, cur in prerequisites:
            graph[cur].append(prev)
        
        cycle = set()
        def dfs(node,target,cycle):
            if node == target:
                return True
            
            if node in cycle:
                return False
            
            cycle.add(node)
            for ni in graph[node]:
                if dfs(ni,target,cycle):return True

            return False
        
        res = []
        for pre,node in queries:
            res.append(dfs(node,pre,set()))
        
        return res



