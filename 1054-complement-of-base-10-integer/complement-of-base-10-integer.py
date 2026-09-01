class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        length=n.bit_length()
        return ((1<<(length))-1)& (~n)