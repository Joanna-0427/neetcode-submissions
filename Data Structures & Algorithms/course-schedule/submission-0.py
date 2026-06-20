class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            preMap = defaultdict(list)
            visited = set()

            for crs, pre in prerequisites:
                preMap[crs].append(pre)
            
            def dfs(crs): #helper函数像是举其中一个例子
                if crs in visited:
                    return False
                
                if preMap[crs] == []:
                    return True
                
                visited.add(crs)
                for pre in preMap[crs]:
                    if not dfs(pre):  #所有pre有一个false，则false// return dfs(pre) 则只检查第一个
                        return False
                
                visited.remove(crs)
                preMap[crs] = []
                return True

            for c in range(numCourses):
                if not dfs(c):
                    return False
            return True
            