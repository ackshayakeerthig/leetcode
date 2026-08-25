class Solution:
    def totalNQueens(self, n: int) -> int:
        # board=[["."]*n for _ in range(n)]
        cols=set()
        diag=set()
        antidiag=set()
        cnt=0
        def nqueens(q):
            nonlocal cnt
            if q==n:
                # ans.append(["".join(line) for line in board])
                cnt+=1
                return
            for i in range(n):
                if issafe(q,i):
                    # board[q][i]="Q"
                    cols.add(i)
                    diag.add(q-i)
                    antidiag.add(q+i)
                    nqueens(q+1)
                    # board[q][i]="."
                    cols.remove(i)
                    diag.remove(q-i)
                    antidiag.remove(q+i)
        def issafe(row,col):
            if col in cols or row-col in diag or row+col in antidiag:
                return False
            return True
        # ans=[]
        nqueens(0)
        return cnt