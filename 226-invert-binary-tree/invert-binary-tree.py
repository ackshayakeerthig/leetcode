# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return root
        def invert(p):
            if p==None:
                return None
            q=TreeNode(p.val)
            q.left=invert(p.right)
            q.right=invert(p.left)
            return  q
        return invert(root)
        