class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        visited=[[0]*cols for _ in range(rows)]
        for i in range(cols):
            if board[0][i] == 'O':
                self.bfs(board, visited, 0, i)
            if board[rows - 1][i] == 'O':
                self.bfs(board, visited, rows - 1, i)
        
        for i in range(rows):
            if board[i][0] == 'O':
                self.bfs(board, visited, i, 0)
            if board[i][cols - 1] == 'O':
                self.bfs(board, visited, i, cols - 1)
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    board[i][j]='X'
    def bfs(self,board,visited,row,col):
        q=deque()
        q.append((row,col))
        visited[row][col]=1
        adjacent=[(1,0),(0,1),(-1,0),(0,-1)]
        while(len(q)>0):
            currow,curcol=q.popleft()
            for drow,dcol in adjacent:
                adjrow,adjcol=drow+currow,dcol+curcol
                if 0<=adjrow<len(board) and 0<=adjcol<len(board[0]) and board[adjrow][adjcol]=='O' and not visited[adjrow][adjcol]:
                    visited[adjrow][adjcol]=1
                    q.append((adjrow,adjcol))

        