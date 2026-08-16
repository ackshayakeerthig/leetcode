class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        count=defaultdict(int)
        for x in nums:
            count[x%space]+=1
        max_count=max(count.values())
        ans=float('inf')
        for x in nums:
            if count[x%space]==max_count:
                ans=min(ans,x)
        return ans