class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD=10**9+7
        words=s.split(' ')
        maxi=max([len(word) for word in words ])

        fact=[1]*(maxi+1)
        for i in range(1,maxi+1):
            fact[i]=(fact[i-1]*i)%MOD
        ans=1
        for word in words:
            ways=fact[len(word)]
            for cnt in Counter(word).values():
                ways = (ways * pow(fact[cnt], MOD - 2, MOD)) % MOD
            ans = (ans * ways) % MOD

        return ans