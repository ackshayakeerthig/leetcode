class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def find(goal):
            if goal<0:
                return 0
            l=0
            r=0
            cnt=0
            mpp=defaultdict(int)
            while r<len(nums):
                mpp[nums[r]]+=1
                while len(mpp)>goal:
                    mpp[nums[l]]-=1
                    if mpp[nums[l]] == 0:
                        del mpp[nums[l]]
                    l+=1
                cnt+=(r-l+1)
                r+=1
            return cnt
        return find(k)-find(k-1)

