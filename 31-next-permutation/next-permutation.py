class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        if sorted(nums,reverse=True)==nums :
            nums[:]=sorted(nums)
            return
        while (i>0):
            if (nums[i]>nums[i-1]):
                val=nums[i-1] 
                # minindex=nums.index(min(nums[i:]))
                minindex=len(nums)-1
                for j in range(len(nums)-1,i-1,-1):
                    if nums[i-1]<nums[j] :
                        minindex=j
                        break
                    
                nums[i-1],nums[minindex]=nums[minindex],nums[i-1]
                nums[:]=nums[:i]+ sorted(nums[i:])
                break
            i-=1
        return
        