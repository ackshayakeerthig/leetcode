class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_of_missing=0
        for i in range(len(nums)):
            xor_of_missing^=nums[i]
        i=0
        
        xor1=0
        xor2=0
        diff_bit=xor_of_missing & -xor_of_missing
        for i in range(len(nums)):
            if nums[i] & diff_bit:
                xor1^=nums[i]
            else:
                xor2^=nums[i]
        return [xor1,xor2]