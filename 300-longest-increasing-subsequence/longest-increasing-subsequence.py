class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp) if dp else 0