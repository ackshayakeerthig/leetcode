class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        quotient=0
        a=abs(dividend)
        b=abs(divisor)
        while a>=abs(divisor):
            b=abs(divisor)
            multiple=1
            while ( b<<1) <= a:
                multiple<<=1
                b<<=1
            quotient+=multiple
            a-=b
        if dividend<0 and divisor <0 or dividend>=0 and divisor>0:
            return quotient
        return -quotient