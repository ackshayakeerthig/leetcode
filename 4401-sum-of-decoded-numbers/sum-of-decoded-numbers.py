class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        width=0
        d=0
        result=0
        MOD=10**9+7
        for i in range(len(nums)):
            width=nums[i]%10
            d=nums[i]//10
            divisor=10**(len(str(d))-width)
            x=d//divisor
            y=d%divisor
            result=(result + pow(x, y, MOD)) % MOD
        return result%MOD
