# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        def dfs(node):
            nonlocal k
            if not node:
                return
            
            l = dfs(node.left)
            if l is not None:
                return l
            k -= 1
            if k == 0:
                return node.val
            r = dfs(node.right)
            if r is not None:
                return r
        
        return dfs(root)