class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        check_even=True
        n=len(nums)
        todelete=0
        for i in range(n):
            if check_even and i%2==0 and i+1<n and nums[i]==nums[i+1]:
                todelete+=1
                check_even=not check_even
            if not check_even and i%2!=0 and i+1<n and nums[i]==nums[i+1]:
                todelete+=1
                check_even=not check_even
        if (n-todelete)%2==0:
            return todelete
        return todelete+1
