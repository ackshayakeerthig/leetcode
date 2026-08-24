class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        n=len(stones)
        memo=defaultdict(bool)
        c0,c1,c2=0,0,0
        for stone in stones:
            if stone%3==0:
                c0+=1
            elif stone%3==1:
                c1+=1
            else:
                c2+=1
        if c0%2==0:
            return (c1>=1 and c2>=1) and (c1>=c2 or c2>=c1)
        return abs(c1-c2)>2
        # def solve(state):
        #     c0,c1,c2=state
        #     if c0+c1+c2<=1 : 
        #         return False
        #     if state in memo:
        #         return memo[state]
        #     if c0>0 and (c1+2*c2)%3!=0:
        #         if  not solve((c0-1,c1,c2)):
        #             memo[state]=True
        #             return True
        #     if c1>0 and (c1-1+2*c2)%3!=0:
        #         if not solve((c0,c1-1,c2)):
        #             memo[state]=True
        #             return True
        #     if c2>0 and (c1+2*(c2-1))%3!=0:
        #         if not solve((c0,c1,c2-1)):
        #             memo[state]=True
        #             return True
        #     memo[state]=False
        #     return False
        # return solve((ini_c0,ini_c1,ini_c2))
            