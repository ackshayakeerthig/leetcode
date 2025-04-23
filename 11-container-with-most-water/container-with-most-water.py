class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        max=0
        while (left < right):
            area=min(height[left],height[right])*(right-left)
            if (area>max):
                max=area
            if (height[left]<height[right]):
                left+=1
            else :
                right-=1
        return max