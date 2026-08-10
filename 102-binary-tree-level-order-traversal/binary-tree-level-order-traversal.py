# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=deque()
        q.append(root)
        answer=[]
        while q:
            subans=[]
            for i in range(len(q)):
                cur=q.popleft()
                subans.append(cur.val)
                if cur.left!=None:
                    q.append(cur.left)
                if cur.right!=None:
                    q.append(cur.right)
            answer.append(subans)
        return answer