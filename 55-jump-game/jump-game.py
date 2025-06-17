class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex=len(nums)-1
        jumpfrom=lastindex-1
        while jumpfrom>=0:
            if jumpfrom+nums[jumpfrom]>=lastindex:
                lastindex=jumpfrom
            jumpfrom-=1
        return lastindex==0