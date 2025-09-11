class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        # digits.sort(reverse=True)
        number=0
        for num in digits:
            number=number *10+num
        number+=1
        print(number)
        final=[]
        while number:
            final.append(number%10)
            number//=10
        final=final[::-1]
        return final