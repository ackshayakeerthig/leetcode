class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)<1:
            return 0
        sign='+'
        if s[0]=='+' or s[0]=='-':
            sign=s[0]
            s=s[1:]
        val=0
        i=0
        while i<len(s) and ord('0')<=ord(s[i])<=ord('9'):
            val=val*10+int(s[i])
            i+=1
        if sign=='-':
            val=-val
        if val<(-2)**31:
            return (-2)**31
        elif val>(2)**31-1:
            return (2)**31-1
        return val