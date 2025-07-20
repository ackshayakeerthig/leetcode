class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        d=sum(nums)
        if d%2!=0:
            return False
        d//=2
        n=len(nums)
        dp=[[-1 for i in range(0,d+1)] for j in range(n)]
        dp[0][0]=1
        for i in range(n):
            dp[i][0]=0
        return bool(self.knapsack(dp,nums,n,d))
    def knapsack(self,dp,nums, n,d):
        if d==0:
            return 1
        if n==0:
            return 0
        value=-1
        if dp[n-1][d]==-1:
            if nums[n-1]>d:
                value=self.knapsack(dp,nums,n-1,d)
            else:
                value=self.knapsack(dp,nums,n-1,d-nums[n-1]) or self.knapsack(dp,nums,n-1,d)
            dp[n-1][d]=value
        return dp[n-1][d]
