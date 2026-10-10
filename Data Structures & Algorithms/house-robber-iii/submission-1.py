# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node):
            if not node:
                return [0,0]
            
            l_contain, l_no = dfs(node.left)
            r_contain, r_no = dfs(node.right)
            n_contain = l_no + r_no + node.val
            n_no = max(l_contain,l_no) + max(r_contain,r_no)

            return [n_contain,n_no]
        
        a,b = dfs(root)
        return max(a,b)


            
