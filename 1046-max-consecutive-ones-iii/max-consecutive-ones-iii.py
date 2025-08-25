class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l=0
        r=0
        maxlen=0
        cnt=0
        while (r<len(nums)):
            if nums[r]==0:
                cnt+=1
            if cnt>k:
                cnt-=1 if nums[l]==0 else 0
                l+=1
            else:             
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen