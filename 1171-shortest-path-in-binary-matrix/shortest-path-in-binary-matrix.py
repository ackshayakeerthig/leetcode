class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=deque()
        q.append((0,0,0))
        visited=[[0]*n for _ in range(n)]
        visited[0][0]=1
        adj=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        if grid[0][0]==1:
            return -1
        while (q):
            dist,x_current,y_current=q.popleft()
            if (x_current,y_current)==(n-1,n-1):
                return dist+1
            for x_add,y_add in adj:
                x_neighbour,y_neighbour=x_current+x_add,y_current+y_add
                if 0<=x_neighbour<n and 0<=y_neighbour<n and grid[x_neighbour][y_neighbour]==0 and not visited [x_neighbour][y_neighbour]:
                    visited[x_neighbour][y_neighbour]=1
                    q.append((dist+1,x_neighbour,y_neighbour))
                    
        return -1