class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #1.判断这两个节点是否在同一个连通块，如果是，则重复；（这两个节点都出现过，并不代表他们是重复，比如出现在两个不同的块）
        #2.寻找连通块：找他们共同的根，如果是同一个则，同一个连通块
        n = len(edges)
        parent = list(range(n+1)) #parent是存的每个节点，根列表；初始每个节点的根是他自己
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b) #两个根节点一样，则已连通
            if ra == rb:
                return [a,b]
            
            parent[ra] = rb #根节点不一样，则建立根节点联系



            
