# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # q = deque()
        # q.append(root)
        # rightside = None

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             rightside = node
        #             if node.left:
        #                 q.append(node.left)
        #             if node.right:
        #                 q.append(node.right)
        #     if rightside:
        #         res.append(rightside.val)
        # return res
              
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                right = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(right)
        return res


        

















