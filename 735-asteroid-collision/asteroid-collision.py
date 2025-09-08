class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        # def stabilise(new):
        #     if not stack:
        #         stack.append(new)
        #         return
        #     if stack and stack[-1]*new >=0:
        #         stack.append(new)
        #         return
        #     if stack and stack[-1]<0:
        #         stack.append(new)
        #         return
        #     if stack and abs(new)<abs(stack[-1]):
        #         return
        #     if stack and abs(new)==abs(stack[-1]):
        #         stack.pop()
        #         return
        #     if stack and abs(new)>abs(stack[-1]):
        #         stack.pop()
        #         stabilise(new)
        for i in range(n):
            # stabilise(nums[i])
            while stack and nums[i]<0<stack[-1]:
                if abs(nums[i])>abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(nums[i])==abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(nums[i])

            # print(stack)
        return stack