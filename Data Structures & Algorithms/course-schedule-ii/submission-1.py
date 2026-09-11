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
            #已经完成搜索并正确的course不能删除清空，后续还要用，所以用visited记录
            visited.add(course)
            #course返回True，并记录course结果，从前➡️后记录
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):return []
        return res


