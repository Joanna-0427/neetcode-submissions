# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        number = 0
        maxval = float('-inf')

        def dfs(node,maxval):
            nonlocal number
            if not node:
                return
            
            if node.val >= maxval:
                number += 1
                maxval = max(maxval,node.val)
            
            dfs(node.left,maxval)
            dfs(node.right,maxval)
        
        dfs(root,maxval)
        return number

