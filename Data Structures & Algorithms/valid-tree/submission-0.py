class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #1.visited的node==n每个node都在Tree中；course里面visited的node可以不是n
        #2.course可以形成环，但是不能形成循环、有终点；所以访问时记录visit，正确后pop；不会影响下一个环；
        #Tree不能形成环，所以已经访问的要记录visit，不能pop；后续判断是否已经访问过，是否是环


        graph = {i:[] for i in range(n)}

        for parent, node in edges:
            graph[parent].append(node)
            graph[node].append(parent)
        
        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                
                if not dfs(neighbour,node):return False
            
            return True
        
        return True if dfs(0,-1) and len(visited) == n else False