# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val == key:
            if root.right:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
            return root.left
        
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        
        return root
            
            
