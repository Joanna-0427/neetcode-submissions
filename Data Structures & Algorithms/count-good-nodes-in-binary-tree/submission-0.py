# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node,maxval):
            nonlocal res
            if not node:
                return
            
            if node.val >= maxval:
                res += 1
            maxval = max(node.val,maxval)

            dfs(node.left,maxval)
            dfs(node.right,maxval)
        
        dfs(root,root.val)
        return res
