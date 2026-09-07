"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}
        def dfs(node):
            #oldtonew类似于visited作用，同时直接返回新copy
            if node in oldtonew:
                return oldtonew[node]
            
            copy = Node(node.val)
            oldtonew[node] = copy
            for nei in node.neighbors:
                #node本身自带的属性neighbors = [],创建时则有了
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node) if node else None
        
