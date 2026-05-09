# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxvalue = float('-inf')
        def dfs(node):
            nonlocal maxvalue
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            leftmax = max(left,0)
            rightmax = max(right,0)
            curr = leftmax + rightmax + node.val
            maxvalue = max(maxvalue,curr)
            return max(leftmax,rightmax) + node.val
        dfs(root)
        return maxvalue