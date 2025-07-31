class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        col0=1
        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]!=0:
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(0,cols):
                matrix[0][j]=0
        if col0==0:
            for i in range(0,rows):
                matrix[i][0]=0
        return matrix