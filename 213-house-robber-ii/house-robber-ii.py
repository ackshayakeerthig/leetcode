class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[0]*n
        if n<=0:
            return 0
        dp[0]=nums[0]
        if n>=2:
            dp[1]=max(nums[0],nums[1])
        else:
            return dp[0]
        for i in range(2,n-1):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        dp2=[0]*n
        if n<=0:
            return 0
        dp2[n-1]=nums[n-1]
        if n>=2:
            dp2[n-2]=max(nums[n-1],nums[n-2])
        else:
            return max(dp2[n-1],dp[0])
        for i in range(n-3,0,-1):
            dp2[i]=max(nums[i]+dp2[i+2],dp2[i+1])
        return max(dp[n-2],dp2[1])
        