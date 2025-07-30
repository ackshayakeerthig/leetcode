class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        nums=set(nums)
        for num in nums:
            count=1
            if num-1 not in nums:
                next=num+1
                while next in nums:
                    count+=1
                    next+=1
                if count>longest:
                    longest=count
        return longest
