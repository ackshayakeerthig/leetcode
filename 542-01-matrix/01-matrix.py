class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        dist=[[float('inf')]*cols for _ in range(rows)]
        # visited=[[0]*cols for _ in range(rows)]
        q=deque()
        for row in range(rows):
            for col in range(cols):
                # if mat[row][col]==0 and not visited[row][col]:
                if mat[row][col]==0 :
                    q.append((row,col,0))
                    # visited[row][col]=1
                    dist[row][col]=0
        adj=[(0,1),(1,0),(0,-1),(-1,0)]
        while (len(q)>0):
            currow,curcol,step=q.popleft()
            for drow,dcol in adj:
                adjrow,adjcol=drow+currow,dcol+curcol
                # if 0<=adjrow<rows and 0<=adjcol<cols and not visited[adjrow][adjcol] and mat[adjrow][adjcol]==1:
                if 0<=adjrow<rows and 0<=adjcol<cols and  mat[adjrow][adjcol]==1 and dist[adjrow][adjcol]>step+1:
                    q.append((adjrow,adjcol,step+1))
                    dist[adjrow][adjcol]=step+1
                    # visited[adjrow][adjcol]=1
            
        return dist