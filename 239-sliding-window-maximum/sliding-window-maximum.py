class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=deque()
        right=0
        for right in range(len(nums)):
            while q and q[0]<right-k+1:
                q.popleft()
            while q and nums[q[-1]]<=nums[right]:
                q.pop()
            q.append(right)

            if right+1>=k:
                ans.append(nums[q[0]])
        return ans