class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[0]*cols for _ in range(rows)]
        dp[0][0]=1
        if grid[0][0]==1:
            return 0
        # if rows>1:
        #     dp[1][0]=1 if grid[1][0] else 0
        # if cols>1:
            dp[0][1]=1 if grid[0][1] else 0
        for i in range(1,rows):
            dp[i][0]=dp[i-1][0] if grid[i][0]!=1 else 0
        for i in range(1,cols):
            dp[0][i]=dp[0][i-1] if grid[0][i]!=1 else 0
        for i in range(1,rows):
            for j in range(1,cols):
                if grid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
            