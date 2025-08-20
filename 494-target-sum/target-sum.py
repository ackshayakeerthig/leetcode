class Solution:
    def findTargetSumWays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        target=(k+sum(nums))
        if target%2==1:
            return 0
        target//=2
        def count(index,target):
            if index==0:
                if target==0 and nums[0]==0:
                    return 2
                return int(target==nums[index] or target==0)
            donttake=count(index-1,target)
            take=0
            if nums[index]<=target:
                take=count(index-1,target-nums[index])
            return donttake+take
        return count(n-1,target)