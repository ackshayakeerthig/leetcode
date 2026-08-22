class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        digit_prod=1
        n_dash=n
        while n:
            digit_sum+=n%10
            digit_prod*=n%10
            n//=10
        return n_dash%(digit_sum+digit_prod)==0
        