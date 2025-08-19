class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2==1:
            return False
        target//=2
        n=len(nums)
        dp=[[-1]*(target+1) for _ in range(n)]
        def find(index,target):
            if target==0:
                return True
            if index==n-1:
                return target==nums[index]
            if dp[index][target]!=-1:
                return dp[index][target]
            donttake=find(index+1,target)
            take=False
            if nums[index]<=target:
                take=find(index+1,target-nums[index])
            dp[index][target]= take or donttake
            return dp[index][target]
        return find(0,target)