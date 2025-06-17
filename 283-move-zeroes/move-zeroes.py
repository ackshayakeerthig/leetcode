class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        n=len(nums)
        while i<n:
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
            else:
                j+=1
            i+=1