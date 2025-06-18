class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=float('-inf')
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max