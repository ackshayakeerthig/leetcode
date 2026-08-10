# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse_equality(a,b):
            if a==None and b==None:
                return True
            elif a==None or b==None:
                return False
            return a.val==b.val and traverse_equality(a.left,b.left) and traverse_equality(a.right,b.right)
        def findmatchinstance(p,q):
            if p==None and q==None:
                return True
            elif p==None or q==None:
                return False
            if p.val==q.val:
                if (traverse_equality(p,q)):
                    return True
            return findmatchinstance(p.left,q) or findmatchinstance(p.right,q)
        return findmatchinstance(root,subRoot)