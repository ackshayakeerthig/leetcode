class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(nums)
        ans=[-1]*n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            ans[i%n]=stack[-1] if stack else -1
            stack.append(nums[i%n])
        return ans