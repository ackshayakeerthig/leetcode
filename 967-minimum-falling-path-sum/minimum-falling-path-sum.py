class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        inf=float('inf')
        for row in range(1,rows):
            for col in range(cols):
                left=matrix[row-1][col-1] if col-1>=0 else  inf
                up=matrix[row-1][col]
                right=matrix[row-1][col+1] if col+1<cols else inf
                matrix[row][col]+=min(left,up,right)
        return min(matrix[-1])
                