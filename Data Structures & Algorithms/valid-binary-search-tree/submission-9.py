# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # def valid(node, low, high):
        #     if not node:
        #         return True

        #     if not (low < node.val < high):
        #         return False
            
        #     left = valid(node.left,low,node.val)
        #     right = valid(node.right,node.val,high)
            
        #     return left and right
        
        # return valid(root,float('-inf'),float('inf'))
        
        def valid(node,low, high):
            if not node:
                return True
            
            if node.val >= high or node.val <= low:
                return False
            
            left = valid(node.left, low, node.val)
            right = valid(node.right,node.val,high)
            return left and right
        
        return valid(root, float('-inf'),float('inf'))
            











        
