class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            
            return parent[a]
        
        for a,b in edges:
            if find(a) != find(b):
                parent[find(a)] = find(b) #把parent[find(a)] 连到find(b)，不然会切断a之前的那棵树
            else:
                return [a,b]
            