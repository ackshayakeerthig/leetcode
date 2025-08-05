class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        ans=[]
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        for key in d:
            if d[key]>n//3:
                ans.append(key)
        return ans