class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[[-1]*cols for _ in range(cols)] for _ in range(rows)]
        def find(i,j1,j2):
            if j1<0 or j2<0 or j1>=cols or j2>=cols:
                return float("-inf")
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            if i==rows-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            maxi=float("-inf")
            val=grid[i][j1]
            if j1!=j2:
                val+=grid[i][j2]
            # for dj1 in range(-1,2):
            #     for dj2 in range(-1,2):
            #         cherries=find(i+1,j1+dj1,j2+dj2)
            #         if cherries>=maxi:
            #             maxi=cherries
            maxi=max(
                find(i+1,j1-1,j2-1),
                find(i+1,j1-1,j2),
                find(i+1,j1-1,j2+1),
                find(i+1,j1,j2-1),
                find(i+1,j1,j2),
                find(i+1,j1,j2+1),
                find(i+1,j1+1,j2-1),
                find(i+1,j1+1,j2),
                find(i+1,j1+1,j2+1),
            )
            dp[i][j1][j2]= maxi+val
            return dp[i][j1][j2]
        ans=find(0,0,cols-1)
        if ans>=0:
            return ans
        return 0