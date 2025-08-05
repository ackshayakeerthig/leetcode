class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=0
        count2=0
        n=len(nums)
        ele1=float('-infinity')
        ele2=float('-infinity')
        for i in range(0,n):
            if count1==0 and ele2!=nums[i]:
                count1=1
                ele1=nums[i]
            elif count2==0 and ele1!=nums[i]:
                count2=1
                ele2=nums[i]
            elif (nums[i]==ele1):
                count1+=1
            elif nums[i]==ele2:
                count2+=1
            else:
                count1-=1
                count2-=1
        count1,count2=0,0
        for num in nums:
            if num==ele1:
                count1+=1
            elif num==ele2:
                count2+=1
        mini=n//3+1
        ans=[]
        if count1>=mini:
            ans.append(ele1)
        if count2>=mini:
            ans.append(ele2)
        ans.sort()
        return ans