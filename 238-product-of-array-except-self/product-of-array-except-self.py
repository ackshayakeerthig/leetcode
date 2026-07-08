class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        prefixmulti=1
        suffixmulti=1
        for i in range(1,n-1):
            prefixmulti*=nums[i-1]
            suffixmulti*=nums[n-i]
            answer[i]*=prefixmulti
            answer[n-i-1]*=suffixmulti
        answer[0]*=suffixmulti*nums[1] if n>1 else 1
        answer[n-1]*=prefixmulti*nums[n-2] if n>1 else 1
        return answer