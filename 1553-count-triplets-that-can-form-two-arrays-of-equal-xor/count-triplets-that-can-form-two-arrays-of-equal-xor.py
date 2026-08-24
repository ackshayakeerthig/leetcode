class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]^arr[i]
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                for k in range(j,n):
                    a=prefix[i]^prefix[j]
                    b=prefix[k+1]^prefix[j]
                    ans+=1 if a==b else 0
        return ans