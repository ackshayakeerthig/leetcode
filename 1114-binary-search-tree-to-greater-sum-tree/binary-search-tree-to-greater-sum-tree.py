# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(node,cur_sum):
            if node==None:
                return 0
            right_sum=solve(node.right,cur_sum)
            node_val=node.val
            node.val=right_sum+cur_sum+node_val
            left_sum=solve(node.left,cur_sum+node_val+right_sum)
            return left_sum+right_sum+node_val
        solve(root,0)
        return root