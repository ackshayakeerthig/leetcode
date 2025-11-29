class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[0 for _ in range(n)]
        dp2=[0 for _ in range(n)]
        dp2[0]=nums[0]
        if n>1:
            dp2[1]=max(dp2[0],nums[1]) 
            dp1[1]=nums[1]
        if n>2:
            dp1[2]=max(nums[1],nums[2])
        for i in range(3,n):
            dp1[i]=max(dp1[i-2]+nums[i], dp1[i-1])
        for i in range(2,n-1):
            dp2[i]=max(dp2[i-2]+nums[i], dp2[i-1])
        return max(dp1[n-1],dp2[n-2])