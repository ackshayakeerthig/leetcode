class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for _ in range(n)]
        rows=n
        cols=n
        count=1
        left,right,top,bottom=0,cols-1,0,rows-1
        while (top<=bottom and left<=right):
            for i in range(left,right+1):
                matrix[top][i]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=count
                count+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=count
                    count+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=count
                    count+=1
                left+=1
        return matrix