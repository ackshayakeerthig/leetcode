class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        
        #binsearch in rows
        up,down=0,rows-1
        while up<=down:
            mid=(up+down)//2
            if matrix[mid][0]>target:
                down=mid-1
            elif matrix[mid][0]==target:
                return True
            else:
                up=mid+1
        row=down
        left,right=0,cols-1
        while left<=right and row >=0:
            mid=(left+right)//2
            if matrix[row][mid]>target:
                right=mid-1
            elif matrix[row][mid]==target:
                return True
            else:
                left=mid+1
        return False
        