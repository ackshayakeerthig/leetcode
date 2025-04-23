def permutation(dic:dict,keys: list,numslen:int,ans:list,temp:list):
    if (len(temp)==numslen):
        ans.append(temp.copy())
    for i in range(0,len(dic)):
        if (dic[keys[i]] <= 0):continue
        temp.append(keys[i])
        dic[keys[i]]-=1
        permutation(dic,keys,numslen,ans,temp)
        dic[keys[i]]+=1
        temp.pop()

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        s=set(nums)
        dic={element : nums.count(element) for element in s }
        permutation(dic,list(dic.keys()),len(nums),ans,[])
        return ans