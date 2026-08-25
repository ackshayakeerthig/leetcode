class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        order_of_freq=list(freq.items())
        order_of_freq.sort(key=lambda x : -x[1])
        n=len(order_of_freq)
        ans=0
        for i in range(n):
            ans+=order_of_freq[i][1]*((i)//8+1)
        return ans