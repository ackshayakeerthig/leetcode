class Solution:
    def numSubarraysWithSum(self, nums: List[int], g: int) -> int:
        def find(goal):         
            if goal <0:
                return 0   
            l,r,cnt,summ=0,0,0,0
            while r<len(nums):
                summ+=nums[r]
                while summ > goal and l<len(nums):
                    summ-=nums[l]
                    l+=1
                cnt+=(r-l+1)
                r+=1
            return cnt
        return find(g)-find(g-1)