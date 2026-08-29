class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly=[1]
        pointers=[0 for i in range(len(primes))]
        for _ in range(n-1):
            mini=float('inf')
            mini_idx=[]
            for i in range(len(primes)):
                if ugly[pointers[i]]*primes[i]<mini:
                    mini=ugly[pointers[i]]*primes[i]
                    mini_idx=[i]
                elif ugly[pointers[i]]*primes[i]<=mini:
                    mini_idx.append(i)
            ugly.append(mini)
            for idx in mini_idx:
                pointers[idx]+=1
        return ugly[-1]