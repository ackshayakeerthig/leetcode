def permutation(nums : List[int], idx : int, ans:List[List[int]] ):
    if (idx==len(nums)-1):
        ans.append(nums.copy())
    for i in range (idx,len(nums)):
        nums[idx],nums[i]=nums[i],nums[idx]
        permutation(nums,idx+1,ans)
        nums[idx],nums[i]=nums[i],nums[idx]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        list=[]
        permutation(nums,0,list)
        return list