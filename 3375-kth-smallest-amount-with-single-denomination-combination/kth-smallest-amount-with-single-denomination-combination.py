class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        if k==0:
            return 0
        left=1
        right=max(coins)*k
        n=len(coins)
        while left<=right:
            mid=(left+right)//2
            count=0
            for mask in range(1,1<<n):
                lcm_val=1
                onbits=0
                for i in range(n):
                    if mask &(1<<i):
                        lcm_val=lcm(lcm_val,coins[i])
                        onbits+=1
                    if lcm_val>mid:
                        break
                if lcm_val<=mid:
                    if onbits%2==0:
                        count-=mid//lcm_val
                    else:
                        count+=mid//lcm_val

            if count<k:
                left=mid+1
            else:
                right=mid-1
        return left