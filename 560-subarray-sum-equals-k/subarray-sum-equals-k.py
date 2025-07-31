class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        presum=0
        d[0]=1
        count=0
        for num in nums:
            presum+=num
            needed=presum-k
            if needed in d:
                count+=d[needed]
            if presum in d:
                d[presum]+=1
            else:
                d[presum]=1
        return count
            
