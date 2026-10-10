# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxleng = 0

        def dfs(node):
            nonlocal maxleng
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            maxleng = max(l + r, maxleng)
            return max(l,r) + 1
        
        dfs(root)
        return maxleng
            
