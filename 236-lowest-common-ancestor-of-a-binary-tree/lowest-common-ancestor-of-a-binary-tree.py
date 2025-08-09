# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def find(current:'TreeNode'):
            nonlocal ans
            if not current:
                 return False
            left=find(current.left)
            right=find(current.right)
            mid=current==p or current==q
            if mid+left+right>=2:
                ans=current
            return left or right or mid
        find(root)
        return ans