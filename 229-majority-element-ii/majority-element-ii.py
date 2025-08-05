class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        ans=[]
        minimum=n//3
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
            if d[num]==minimum+1:
                ans.append(num)

        return ans

        