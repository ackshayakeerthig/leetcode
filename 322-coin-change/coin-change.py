class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        INF = 10**9  # sentinel for impossible
        prev = [INF] * (amount + 1)
        cur = [INF] * (amount + 1)
        for t in range(amount+1):
            if t%coins[0]==0:
                prev[t]=t//coins[0]
        for i in range(1,n):
            for j in range(amount+1):
                donttake=prev[j]
                take=INF
                if coins[i]<=j:
                    take=1+cur[j-coins[i]]
                cur[j]=min(take,donttake)
            cur,prev=prev,cur
        return prev[amount] if prev[amount]!=INF else -1
        
        # @lru_cache()
        # def find(index,amount):
        #     if index==0:
        #         if amount%coins[index]==0:
        #             return amount//coins[index]
        #         return 10**9
        #     if amount==0:
        #         return 0
        #     nottake=find(index-1,amount)
        #     take=10**9
        #     if coins[index]<=amount:
        #         take=1+find(index,amount-coins[index])
        #     return min(take,nottake)
        # ans=find(n-1,amount)
        # return ans if ans!=10**9 else -1