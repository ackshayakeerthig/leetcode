class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        h=[]
        m=len(matrix)
        n=len(matrix[0])
        if m<1 or n<1:
            return 0
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    pass
                elif i==0:
                    matrix[i][j]=matrix[i][j]^matrix[i][j-1]
                elif j==0:
                    matrix[i][j]=matrix[i][j]^matrix[i-1][j]

                else:
                    matrix[i][j]=matrix[i][j]^matrix[i][j-1]^matrix[i-1][j]^matrix[i-1][j-1]

                heapq.heappush(h,matrix[i][j])
                if len(h)>k:
                    heapq.heappop(h)
        print(h)
        return h[0]