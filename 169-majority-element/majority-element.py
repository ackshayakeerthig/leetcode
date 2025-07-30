class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=nums[0]
        count=0
        for num in nums:
            
            if count==0:
                maj=num
            if num==maj:
                count+=1
            else:
                count-=1
        return maj
        