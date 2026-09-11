class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c:[] for c in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        res = []
        visited, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            #如果是空，直接跳过并返回True，不会报错，
            for pre in graph[course]:
                if not dfs(pre): return False
            
            cycle.remove(course)

            #剪枝，已经True的直接记为visited
            visited.add(course)

            #从前--后记录course结果，
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):return []
        return res


