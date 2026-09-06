class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        if not matrix :
            return False
        cols=len(matrix[0])
        left=0
        right=rows*cols-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid//cols][mid%cols]<target:
                left=mid+1
            elif matrix[mid//cols][mid%cols]>target:
                right=mid-1
            else:
                return True
        return False