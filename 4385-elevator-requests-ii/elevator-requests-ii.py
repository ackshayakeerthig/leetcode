class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        requests=[x for x in requests if x!=start]
        pos=sorted(requests+[start])
        n=len(pos)
        s=pos.index(start)
        is_req=[1 if x!=start else 0 for x in pos]
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+is_req[i]
        def remaining(l,r):
            return len(requests)-(prefix[r+1]-prefix[l])
        dp=[[[float('inf')]*2 for _ in range(n)] for _ in range(n)]
        dp[s][s][0]=dp[s][s][1]=0

        for length in range(2,n+1):
            for left in range(max(0,s-length+1),s+1):
                right=left+length-1
                if right>=n or not (left<=s<=right):
                    continue
                
                if left<s:
                    rem=remaining(left+1,right)
                    dp[left][right][0]=min(dp[left][right][0],dp[left+1][right][0]+(pos[left+1]-pos[left])*rem,dp[left+1][right][1]+(pos[right]-pos[left])*rem)
                if right>s:
                    rem=remaining(left,right-1)
                    dp[left][right][1]=min(dp[left][right][1],dp[left][right-1][0]+(pos[right]-pos[left])*rem,dp[left][right-1][1]+(pos[right]-pos[right-1])*rem)
        return min(dp[0][n-1])