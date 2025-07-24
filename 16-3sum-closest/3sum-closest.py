class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        summ=0
        closest=float('inf')
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while (left<right):
                total=nums[i]+nums[left]+nums[right]
                difference=abs(total-target)
                if difference<closest:
                    summ=total
                    closest=difference
                elif difference==0:
                    return total
                if total<target:
                    left+=1
                if total>target:
                    right-=1
        return summ
        