class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        next_g=[0]*n
        next_s=[0]*n
        prev_g=[0]*n
        prev_s=[0]*n
        def next_greater():
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and nums[i]>=nums[stack[-1]]:
                    stack.pop()
                next_g[i]=stack[-1] if stack else n
                stack.append(i)
        def next_smaller():
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and nums[i]<=nums[stack[-1]]:
                    stack.pop()
                next_s[i]=stack[-1] if stack else n
                stack.append(i)
        
        def prev_greater():
            stack=[]
            for i in range(0,n):
                while stack and nums[i]>nums[stack[-1]]:
                    stack.pop()
                prev_g[i]=stack[-1] if stack else -1
                stack.append(i)
        
        def prev_smaller():
            stack=[]
            for i in range(n):
                while stack and nums[i]<nums[stack[-1]]:
                    stack.pop()
                prev_s[i]=stack[-1] if stack else -1
                stack.append(i)
        next_greater()
        next_smaller()
        prev_greater()
        prev_smaller()
        sum_largest=0
        sum_smallest=0
        def sum_max():
            nonlocal sum_largest
            for i in range(n):
                left=prev_g[i]
                right=next_g[i]
                sum_largest+=(i-left)*(right-i)*(nums[i])
        def sum_min():
            nonlocal sum_smallest
            for i in range(n):
                left=prev_s[i]
                right=next_s[i]
                sum_smallest+=(i-left)*(right-i)*(nums[i])
        sum_max()  
        sum_min()  
        return sum_largest-sum_smallest
        