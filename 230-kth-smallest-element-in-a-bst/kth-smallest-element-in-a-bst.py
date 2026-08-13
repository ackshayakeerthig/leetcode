# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=[0]
        def inorder(p,c):
            if p==None:
                return None
            left=inorder(p.left,c)
            #traverse p
            if c[0]==k:
                return left
            c[0]+=1
            if c[0]==k:
                return p.val
            right=inorder(p.right,c)
            if c[0]==k:
                return right
            return None
        answer=inorder(root,count)
        return answer