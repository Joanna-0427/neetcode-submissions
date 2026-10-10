# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval = float('-inf')

        def dfs(node):
            nonlocal maxval
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            maxleft = max(l,0)
            maxright = max(r,0)
            maxval = max(maxval,maxleft+maxright+node.val)

            return max(maxleft,maxright) + node.val
        
        dfs(root)
        return maxval