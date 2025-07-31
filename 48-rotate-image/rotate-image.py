class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        new=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                new[j][cols-i-1]=matrix[i][j]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=new[i][j]
        