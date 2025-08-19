class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subsets=[]
        for include in range(2**n):
            test_include=include
            subset=[]
            for num in nums:
                if test_include%2==1:
                    subset.append(num)
                test_include>>=1
            subsets.append(subset)
        return subsets