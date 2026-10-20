class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        graph = defaultdict(list)

        for pre, cur in prerequisites:
            graph[cur].append(pre)
        
        visited = set() #每个节点都搜一遍，路径可能指数级，加visited，每个节点只搜一次
        def dfs(node,target,visited):
            if node == target:
                return True

            visited.add(node)
            for ni in graph[node]:
                if ni not in visited and dfs(ni,target,visited):
                    return True
            
            return False
        
        for p, c in queries:
            res.append(dfs(c,p,set())) #不同搜索条件，visited清空；同一个搜索条件visited不用清空
        return res