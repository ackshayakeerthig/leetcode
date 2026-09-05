class Solution:
    def climbStairs(self, n: int) -> int:
        prev_of_prev=1
        if n==1:
            return 1
        prev=2
        if n==2:
            return 2
        cur=None
        for i in range(2,n):
            cur=prev_of_prev+prev
            prev_of_prev=prev
            prev=cur
        return cur
        