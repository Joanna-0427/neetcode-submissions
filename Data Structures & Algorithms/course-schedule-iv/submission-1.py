class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = {i:[] for i in range(numCourses)}
        for prev,course in prerequisites:
            graph[course].append(prev)
        
        #如果queries很长，全都要重算一遍；重新递归到底dfs查询
        #把课程的所有前置prev在dfs时一次存入表memo，直接查询该表
        memo = {}
        def dfs(course):
            if course not in memo:
                memo[course] = set()
                for prev in graph[course]:
                    memo[course].add(prev)
                    memo[course] |= dfs(prev) #集合元素的合并2:{4,3},4:{5,6},3:{} 合并后2:{4,3,5,6}

            return memo[course]
        
        for i in range(numCourses):
            dfs(i)

        res = []
        for prev, crs in queries:
            res.append(prev in memo[crs])
        return res


        # def dfs(course,target):
        #     if course == target:
        #         return True
            
        #     for prev in graph[course]:
        #         if dfs(prev,target):
        #             return True
            
        #     return False

        # for pre, crs in queries:
        #     res.append(dfs(crs,pre))
        # return res
            
