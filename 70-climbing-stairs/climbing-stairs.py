import math
def fact(n):
    return math.factorial(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        sum=0
        i=0
        while (abs(2*i)+abs(1*(n-2*i))==n):
            p=fact(n-i)/(fact(n-2*i)*fact(i))
            
            sum+=p
            i+=1
        return int(sum)