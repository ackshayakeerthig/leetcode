class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(32):
            count=0
            for num in nums:
                if num & (1<<i):
                    count+=1
            if count%3==1:
                ans|=(1<<i)
        if ans>=2**31:
            ans-=2**32
        return ans