# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []

        while q: #q不是[]:false，[null]:True
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)  #left可能是null
                    q.append(cur.right)  #right可能是null
            if level:
                res.append(level)
        return res
            
            



                
