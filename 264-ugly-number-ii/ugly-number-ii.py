class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==0:
            return 0
        ugly_nums=[1]
        i2=0
        i3=0
        i5=0
        while len(ugly_nums)<n:
            mini=min(ugly_nums[i2]*2,ugly_nums[i3]*3,ugly_nums[i5]*5)
            ugly_nums.append(mini)
            if mini==ugly_nums[i2]*2:
                i2+=1
            if mini==ugly_nums[i3]*3:
                i3+=1
            if mini==ugly_nums[i5]*5:
                i5+=1
        return ugly_nums[-1]

