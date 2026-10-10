# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        cur = root
        if cur.val < val:
            cur.right = self.insertIntoBST(cur.right,val)
        elif cur.val > val:
            cur.left = self.insertIntoBST(cur.left,val)
        
        return root
        
