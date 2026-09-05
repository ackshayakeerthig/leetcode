class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if not nums:
            return -1
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=max(prefix[i-1],nums[i])
        mini=nums[n-1]
        score=-1
        for i in range(n-1,-1,-1):
            mini=min(mini,nums[i])
            if prefix[i]-mini<=k:
                score=i
        return score