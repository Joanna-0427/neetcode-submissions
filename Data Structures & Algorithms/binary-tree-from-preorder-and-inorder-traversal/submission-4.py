# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #hashmap查询idx 比inorder.index() 查询快
        inorder_idx = {val:i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left,right):
            # left, right 是inorder数组里, 当前这棵子树对应的范围(下标)
            if left > right:
                return

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            
            mid = inorder_idx[root_val] # O(1)查找, 不再用.index()
            
            node.left = build(left,mid-1)  
            node.right = build(mid+1,right)
            return node
        
        return build(0,len(inorder)-1)