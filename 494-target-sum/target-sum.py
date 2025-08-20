class Solution:
    def findTargetSumWays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        target=(k+sum(nums))
        if target%2==1:
            return 0
        target//=2
        dp=[[-1]*(target+1) for _ in range(n)]
        def count(index,target):
            if target<0:
                return 0
            if dp[index][target]!=-1:
                return dp[index][target]
            if index == 0:
                if target == 0 and nums[0] == 0:
                    dp[index][target] = 2
                elif target == 0 or target == nums[0]:
                    dp[index][target] = 1
                else:
                    dp[index][target] = 0
                return dp[index][target]
            donttake=count(index-1,target)
            take=0
            if nums[index]<=target:
                take=count(index-1,target-nums[index])
            dp[index][target]= donttake+take
            return dp[index][target]
        return count(n-1,target)