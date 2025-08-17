class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        def nqueens(q):
            if q==n:
                display()
                return
            for i in range(n):
                if issafe(q,i):
                    board[q][i]="Q"
                    nqueens(q+1)
                    board[q][i]="."
                else:
                    continue
        def issafe(row,col):
            for i in range(row):
                if board[i][col]=="Q":
                    return False
            i,j=row-1,col-1
            while (i>=0 and j>=0):
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            i,j=row-1,col+1
            while (i>=0 and j<n):
                if board[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True
        ans=[]
        def display():
            valid_board=[]
            for line in board:
                valid_board.append("".join(line))
            ans.append(valid_board)
        nqueens(0)
        return ans