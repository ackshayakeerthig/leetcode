class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # n1=int(num1)
        # n2=int(num2)
        # return str(n1*n2)
        n1=0
        n2=0
        for char in num1:
            n1=n1*10+(ord(char)-ord("0"))
        for char in num2:
            n2=n2*10+ord(char)-ord("0")
        result=n1*n2
        return str(n1*n2)

        