class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            cnt=0
            cur=0
            for num in nums:
                if num<=bound:
                    cur+=1
                    cnt+=cur
                else:
                    cur=0
            return cnt
        return count(right)-count(left-1)