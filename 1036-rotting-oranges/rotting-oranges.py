class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min=float('inf')
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col]==2:
                    visited[row][col]=1
                    q.append((row,col,0))
                if grid[row][col]==1:
                    fresh+=1
        adjacent=[(0,1),(1,0),(0,-1),(-1,0)]
        lasttime=0
        while (len(q)>0):
            currow,curcol,time=q.popleft()
            for drow , dcol in adjacent:
                adjrow,adjcol=currow+drow,curcol+dcol
                if 0<=adjrow<rows and 0<=adjcol<cols and not visited[adjrow][adjcol] and grid[adjrow][adjcol]==1:
                    visited[adjrow][adjcol]=1
                    grid[adjrow][adjcol]=2
                    fresh-=1
                    q.append((adjrow,adjcol,time+1))
                    lasttime=time+1
        if fresh==0:
            return lasttime
        return -1

