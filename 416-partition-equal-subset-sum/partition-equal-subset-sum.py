class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2==1:
            return False
        target//=2
        n=len(nums)
        if n==0:
            return False
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
