# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)!=len(postorder):
            return None
        hashmap={}
        for i in range(len(inorder)):
            hashmap[inorder[i]]=i
        def build(i_start,i_end,p_start,p_end):
            if i_start>i_end or p_start > p_end:
                return None
            cur_node=TreeNode(postorder[p_end])
            cur_node.left=build(i_start,hashmap[cur_node.val]-1,p_start,p_start+hashmap[cur_node.val]-i_start-1)
            cur_node.right=build(hashmap[cur_node.val]+1,i_end,p_start+hashmap[cur_node.val]-i_start,p_end-1)
            return cur_node
        return build(0,len(inorder)-1,0,len(postorder)-1)
            

        