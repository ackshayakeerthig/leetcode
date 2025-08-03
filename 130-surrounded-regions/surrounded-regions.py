class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows,cols=len(board),len(board[0])
        adjacent=[()]
        def dfs(row,col):
            if 0<=row<rows and 0<=col<cols and board[row][col]=='O':
                board[row][col]='#'
                dfs(row+1,col)
                dfs(row,col+1)
                dfs(row-1,col)
                dfs(row,col-1)
        for i in range(rows):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][cols-1]=='O':
                dfs(i,cols-1)
        for i in range(cols):
            if board[0][i]=='O':
                dfs(0,i)
            if board[rows-1][i]=='O':
                dfs(rows-1,i)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='#':
                    board[row][col]='O'
                elif board[row][col]=='O':
                    board[row][col]='X'
