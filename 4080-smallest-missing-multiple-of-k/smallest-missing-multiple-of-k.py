class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash=defaultdict(bool)
        for i in range(len(nums)):
            if nums[i]%k==0:
                hash[nums[i]//k]=True
        for i in range(1,len(nums)+1):
            if i not in hash:
                return i*k
        return (len(nums)+1)*k
                