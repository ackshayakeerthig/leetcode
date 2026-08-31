class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        already_seen={nums[0]}
        ans=set(nums)
        n=len(nums)
        prev=nums[0]
        for i in range(1,n):
            if prev!=nums[i]:
                if nums[i] not in already_seen:
                    already_seen.add(nums[i])
                else:
                    ans.discard(nums[i])
            prev=nums[i]
        return len(ans)