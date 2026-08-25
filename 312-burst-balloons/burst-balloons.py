class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        
        for length in range(3,n+1):
            for left in range(0,n-length+1):
                right=left+length-1
                for k in range(left+1,right):
                    dp[left][right]=max(dp[left][right],dp[left][k]+dp[k][right]+nums[left]*nums[k]*nums[right])
        return dp[0][n-1]