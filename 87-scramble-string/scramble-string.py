class Solution:
    def isScramble(self, given: str,target: str) -> bool:
        memo={}
        def solve(cur,target):
            if (cur,target) in memo:
                return memo[(cur,target)]
            if cur==target:
                return True
            if len(cur)==1:
                return False
            if sorted(cur)!=sorted(target):
                return False
            for i in range(1,len(cur)):
                swap=solve(cur[:i],target[len(target)-i:]) and solve(cur[i:],target[:len(target)-i])
                notswap=solve(cur[:i],target[:i]) and solve(cur[i:],target[i:])
                if swap or notswap:
                    memo[(cur,target)]=True
                    return memo[(cur,target)]
            memo[(cur,target)]=False
            return memo[(cur,target)]
        return solve(given,target)