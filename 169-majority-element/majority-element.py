class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        repeated=0
        element=None
        for num in nums:
            if repeated==0:
                element=num
            if element==num:
                repeated+=1
            else:
                repeated-=1
        return element