class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        suffix=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i]=suffix[i+1]+piles[i]
        memo={}
        def find(i,M):
            if i>=n:
                return 0
            if (i,M) in memo:
                return memo[(i,M)]
            best=0
            for x in range(1,2*M+1):
                new_M=max(M,x)
                if i+x>n:
                    break
                opponent=find(i+x,new_M)
                current=suffix[i]-opponent
                best=max(best,current)
            memo[(i,M)]=best
            return memo[(i,M)]
        return find(0,1)