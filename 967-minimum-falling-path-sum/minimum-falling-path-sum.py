class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        adjacent=[(-1,0),(-1,1),(-1,-1)]
        for i in range(1,rows):
            for j in range(cols):
                minn=float('inf')
                for drow,dcol in adjacent:
                    row,col=i+drow,j+dcol
                    if 0<=row<rows and 0<=col<cols and matrix[row][col]<=minn:
                        minn=matrix[row][col]
                matrix[i][j]+=minn
        return min(matrix[-1])
                