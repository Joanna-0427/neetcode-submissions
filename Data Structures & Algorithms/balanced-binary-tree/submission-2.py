# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [0,True]
            
            l_val, l_bool = dfs(node.left)
            r_val, r_bool = dfs(node.right)
            length = max(l_val,r_val)
            if not l_bool or not r_bool or abs(l_val - r_val) > 1:
                return [length + 1, False]
            return [length+1, True]
        
        return dfs(root)[1]

                


        
        