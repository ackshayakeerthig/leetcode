class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts=[0] +sorted(cuts)+[n]
        m=len(cuts)
        dp=[[float('inf')]*m for _ in range(m)]
        for i in range(m-1):
            dp[i][i+1]=0
        for interval_length in range(3,m+1):
            for left in range(m-interval_length+1):
                right=left+interval_length-1
                curcost=cuts[right]-cuts[left]
                for k in range(left+1,right):
                    dp[left][right]=min(dp[left][right],dp[left][k]+dp[k][right]+curcost)
        return dp[0][m-1]
