class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        left=1
        MOD=10**9+7
        right=max(a,b)*n
        lcm=math.lcm(a,b)
        while left<=right:
            mid=(left+right)//2
            #countleft
            count=mid//a+mid//b-mid//lcm
            if count>=n:
                right=mid-1
            else:
                left=mid+1
        return left%MOD