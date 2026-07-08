# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not subRoot:
        #     return True
        # if not root:
        #     return False

        # def issame(p,q):
        #     if not p and not q:
        #         return True
        #     if not p or not q:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     return (issame(p.left,q.left) and issame(p.right,q.right))
        
        # if root.val == subRoot.val and issame(root,subRoot):
        #     return True
        
        # return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


        if not root:
            return False
        
        if not subRoot:
            return True
        
        if self.isSame(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        l = self.isSame(p.left,q.left)
        r = self.isSame(p.right,q.right)
        return l and r
        
        