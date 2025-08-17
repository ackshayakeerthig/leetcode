class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # for row in range(1,len(triangle)):
        #     no_ele=len(triangle[row])
        #     triangle[row][0]+=triangle[row-1][0]
        #     triangle[row][-1]+=triangle[row-1][-1]
        #     for i in range(1,no_ele-1):
        #         triangle[row][i]+=min(triangle[row-1][i],triangle[row-1][i-1])
        # return min(triangle[-1])
        n=len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]