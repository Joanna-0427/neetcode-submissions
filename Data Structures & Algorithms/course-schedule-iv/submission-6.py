class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        graph = defaultdict(list)

        for pre, cur in prerequisites:
            graph[cur].append(pre)
        
        seen = set() #每个节点都搜一遍，路径可能指数级，加seen，每个节点只搜一次,有点像之前的visited，已经看过了，有就该早返回了
        def dfs(node,target,seen):
            if node == target:
                return True

            seen.add(node)
            for ni in graph[node]:
                if ni not in seen and dfs(ni,target,seen):
                    return True
            
            return False
        
        for p, c in queries:
            res.append(dfs(c,p,set())) #不同搜索条件，visited清空；同一个搜索条件visited不用清空
        return res