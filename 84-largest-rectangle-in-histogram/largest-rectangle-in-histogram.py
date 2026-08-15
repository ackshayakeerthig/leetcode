class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        n=len(height)
        stack=[]
        maxarea=0
        for i in range(n):
            while stack and height[i]<height[stack[-1]]:
                h=height[stack.pop()]
                width=i-stack[-1]-1 if stack else i
                maxarea=max(maxarea,h*width)
            stack.append(i)
        stacklen=len(stack)
        while stack:
            h=height[stack.pop()]
            width=n -stack[-1]-1 if stack else n
            maxarea=max(maxarea,h*width)
        return maxarea
