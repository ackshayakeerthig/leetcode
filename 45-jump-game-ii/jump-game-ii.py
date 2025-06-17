class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:return 0
        totaljumps=0
        lastindex=len(nums)-1
        jumpfrom=lastindex-1
        while jumpfrom>=0:
            if jumpfrom+nums[jumpfrom]>=lastindex :
                i=0
                while i<jumpfrom:
                    if i+nums[i]>=lastindex and i<jumpfrom:
                        jumpfrom=i
                        break
                    i+=1
                lastindex=jumpfrom
                totaljumps+=1
            jumpfrom-=1
        return totaljumps