class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2==1:
            return False
        target//=2
        n=len(nums)
        if n==0:
            return False
        # dp=[[-1]*(target+1) for _ in range(n)]
        cur=[False]*(target+1)
        prev=[False]*(target+1)
        prev[0]=cur[0]=True
        if nums[0]<=target:
            prev[nums[0]]=True
        for i in range(1,n):
            for j in range(1,target+1):
                nottake=prev[j]
                take=False
                if nums[i]<=j:
                    take=prev[j-nums[i]]
                cur[j]=take or nottake
            prev,cur=cur,prev
        return prev[target]

        # def find(index,target):
        #     if target==0:
        #         return True
        #     if index==0:
        #         return target==nums[index]
        #     if dp[index][target]!=-1:
        #         return dp[index][target]
        #     donttake=find(index-1,target)
        #     take=False
        #     if nums[index]<=target:
        #         take=find(index-1,target-nums[index])
        #     dp[index][target]= take or donttake
        #     return dp[index][target]
        # return find(n-1,target)