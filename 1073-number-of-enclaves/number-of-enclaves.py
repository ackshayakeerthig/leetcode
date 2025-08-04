class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if 0<=r<rows and 0<=c<cols and grid[r][c]==1:
                grid[r][c]=0
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)
        for i in range(rows):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][cols-1]==1:
                dfs(i,cols-1)
        for j in range(cols):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[rows-1][j]==1:
                dfs(rows-1,j)
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count+=1
        return count