class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        teststr=[]
        for char in s:
            if char.isalnum():
                teststr.append(char.lower())
        return teststr[::-1]==teststr[::]