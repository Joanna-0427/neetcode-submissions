# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # q = deque()
        # q.append(root)
        # res = []

        # while q: #q不是[]:false，[null]:True
        #     level = []
        #     for i in range(len(q)):
        #         cur = q.popleft()
        #         if cur:
        #             level.append(cur.val)
        #             q.append(cur.left)  
        #             q.append(cur.right)  
        #     if level:  left，right同时为null，level=[]
        #         res.append(level)
        # return res
        
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(level)
        return res
            















                
