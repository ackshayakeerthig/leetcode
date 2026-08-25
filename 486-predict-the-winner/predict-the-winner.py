class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+1)]
        mem={}
        def solve(i,j):
            if i>=j:
                return 0
            if (i,j) in mem:
                return mem[(i,j)]
            mem[(i,j)]=max(nums[i]-solve(i+1,j),nums[j]-solve(i,j-1))
            return mem[(i,j)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
        # return solve(0,n-1)>=0
        return dp[0][n-1]>=0