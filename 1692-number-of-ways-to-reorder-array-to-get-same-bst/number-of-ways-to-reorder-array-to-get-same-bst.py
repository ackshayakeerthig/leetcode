class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        if not nums :
            return 0
        MOD=10**9+7
        n=len(nums)
        C=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            C[i][0]=1
            C[i][i]=1
            for j in range(1,i):
                C[i][j]=(C[i-1][j-1]+C[i-1][j])%MOD
        class Node():
            def __init__(self,val=None):
                self.val=val
                self.left=None
                self.right=None
        root=Node(nums[0])
        def insert(node,val):
            if node.val>=val:
                if node.left==None:
                    node.left=Node(val)
                else :
                    insert(node.left,val)
            elif node.val<val:
                if node.right==None:
                    node.right=Node(val)
                else:
                    insert(node.right,val)
        for num in nums[1:]:
            insert(root,num)
        def dfs(node):
            if node==None:
                return (0,1)
            left_nodes,left_ways=dfs(node.left)
            right_nodes,right_ways=dfs(node.right)
            return (left_nodes+right_nodes+1,(left_ways*right_ways*C[left_nodes+right_nodes][left_nodes])%MOD)
        return dfs(root)[1]-1