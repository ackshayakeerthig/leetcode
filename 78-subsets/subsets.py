def subset(nums : list, ans:list,temp:list,idx):
    if (idx==len(nums)):
        ans.append(temp)
        return 
    # temp.append()
    subset(nums,ans,temp+[nums[idx]],idx+1)
    subset(nums,ans,temp,idx+1)
    # temp.pop()
    # subset(nums,ans,temp,idx+1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        subset(list(set(nums)),l,[],0)
        return l