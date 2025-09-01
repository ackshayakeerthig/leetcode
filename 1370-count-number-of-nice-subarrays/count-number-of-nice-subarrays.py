class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def find(goal):
            if goal<0:
                return 0
            summ,cnt,l,r=0,0,0,0
            while r<len(nums):
                summ+=nums[r]%2
                while summ > goal:
                    summ-=nums[l]%2
                    l+=1
                cnt+=(r-l+1)
                r+=1

            return cnt
        return find (k)-find(k-1)