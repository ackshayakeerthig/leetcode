class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1 for x in range(len(nums))]
        return self.find(nums, len(nums)-1,dp)
    def find(self, nums:list,houseno:int,dp:list):
        if houseno==0:
            dp[0]=nums[0]
        if houseno==1:
            dp[1]=max(nums[0],nums[1])
        if dp[houseno]!=-1:
            return dp[houseno]
        dp[houseno]= max(self.find(nums,houseno-1,dp),self.find(nums,houseno-2,dp)+nums[houseno])
        return dp[houseno]