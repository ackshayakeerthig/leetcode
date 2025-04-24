def subset(nums:list,ans:list,temp:list,idx:int,d:dict):
    if (len(nums)==idx):
        ans.append(temp[:]) 
        return
    if d[nums[idx]]==1:
        subset(nums,ans,temp+[nums[idx]],idx+1,d)
    d[nums[idx]]=0
    subset(nums,ans,temp,idx+1,d)
    d[nums[idx]]=1
    

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        d={n : 1 for n in set(nums)}
        subset(nums,ans,[],0,d)
        return ans

