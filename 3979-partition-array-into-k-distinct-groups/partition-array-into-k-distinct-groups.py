class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n%k!=0:
            return False
        freq=Counter(nums)
        nums.sort(key=lambda x: -freq[x])
        no_of_grps=n//k
        if max(freq.values())>no_of_grps:
            return False
        return True
        # groups=[set() for _ in range(no_of_grps)]

        # def solve(i):
        #     if i==n:
        #         return True
        #     x=nums[i]
        #     for group in groups:
        #         if len(group)==k:
        #             continue
        #         if x in group:
        #             continue
        #         group.add(x)
        #         if solve(i+1):
        #             return True
        #         group.remove(x)
        #         if len(group)==0:
        #             break
        #     return False
        # return solve(0)