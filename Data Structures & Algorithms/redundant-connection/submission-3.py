class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]

        #不断的寻找它的祖先根
        def find(x):
            #使用while循环，减少递归占用的stack空间
            while x != par[x]:
                x = par[x]  #返回找到的祖先
            return x
        
        for node1,node2 in edges:
            #两者是同一个祖先（已经在同一个环里）
            if find(node1) == find(node2):
                return [node1,node2]
        
            #两个没有同一个祖先，则表明他们之前没有连通过，可以连接
            #find(node1)根的指向更换
            par[find(node1)] = find(node2)
        return []
            


