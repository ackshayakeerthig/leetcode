class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # d={}
        # for i in range(len(nums)):
        #     needed=target-nums[i]
        #     if needed in d:
        #         return [d[needed],i]
        #     d[nums[i]]=i
        # return -1
        d = {}
        append = d.__setitem__  # Faster than d[num] = i
        get = d.get              # Faster than "in d"
        
        for i, num in enumerate(nums):
            match = get(target - num)
            if match is not None:
                return [match, i]
            append(num, i)
        return []
