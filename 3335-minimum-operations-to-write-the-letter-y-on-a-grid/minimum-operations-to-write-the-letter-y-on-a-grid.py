class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n=len(grid)
        non_y=defaultdict(int)
        y=defaultdict(int)
        for i in range(n):
            for j in range(n):
                if((i==j or i==n-j-1 ) and i<=n//2) or (j==n//2 and i>n//2):
                    y[grid[i][j]]+=1
                else:
                    non_y[grid[i][j]]+=1
        maxi=0
        for key1 in y:
            for key2 in non_y:
                if key1!=key2:
                    maxi=max(y[key1]+non_y[key2],maxi)
        if maxi==0:
            return n+n//2
        return n*n-maxi