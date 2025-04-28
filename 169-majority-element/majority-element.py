class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        d={nums.count(x): x  for x in s}
        return d[max(list(d.keys()))]
        