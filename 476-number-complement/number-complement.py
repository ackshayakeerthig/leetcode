class Solution:
    def findComplement(self, num: int) -> int:
        if num==0:
            return 1
        return ((1<<num.bit_length())-1)& (~num)