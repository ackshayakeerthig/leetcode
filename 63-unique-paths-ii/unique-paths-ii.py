class Solution:
    def uniquePathsWithObstacles(self, obstacle: List[List[int]]) -> int:
        rows=len(obstacle)
        cols=len(obstacle[0])
        dp=[[-1]*cols for _ in range(rows)]
        return self.findways(dp,obstacle,rows-1,cols-1)
    def findways(self,dp,obstacle,m,n):
        if dp[m][n]==-1:
            if m==0 and n==0:
                dp[m][n]=0 if obstacle[m][n]==1 else 1
            elif m==0:
                dp[m][n]= 0 if obstacle[m][n]==1 else self.findways(dp,obstacle,m,n-1) 
            elif n==0:
                dp[m][n]=0 if obstacle[m][n]==1 else self.findways(dp,obstacle,m-1,n) 
            else:
                dp[m][n]=0 if obstacle[m][n]==1 else self.findways(dp,obstacle,m,n-1) +self.findways(dp,obstacle,m-1,n)
        return dp[m][n]