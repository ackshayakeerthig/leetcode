class Solution:
    def findTargetSumWays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        target=(k+sum(nums))
        if target%2==1 or target<0:
            return 0
        target//=2
        dp=[[0]*(target+1) for _ in range(n)]
        # for i in range(n):
        #     dp[i][0]=1
        
        dp[0][0]=1
        if nums[0]==0:
            dp[0][0]=2
        if nums[0]!=0 and nums[0]<=target:
            dp[0][nums[0]]=1
        for i in range(1,n):
            for j in range(target+1):
                dp[i][j]=dp[i-1][j]
                if nums[i]<=j:
                    dp[i][j]+=dp[i-1][j-nums[i]]
        return dp[n-1][target]
        # def count(index,target):
        #     if target<0:
        #         return 0
        #     if dp[index][target]!=-1:
        #         return dp[index][target]
        #     if index == 0:
        #         if target == 0 and nums[0] == 0:
        #             dp[index][target] = 2
        #         elif target == 0 or target == nums[0]:
        #             dp[index][target] = 1
        #         else:
        #             dp[index][target] = 0
        #         return dp[index][target]
        #     donttake=count(index-1,target)
        #     take=0
        #     if nums[index]<=target:
        #         take=count(index-1,target-nums[index])
        #     dp[index][target]= donttake+take
        #     return dp[index][target]
        # return count(n-1,target)