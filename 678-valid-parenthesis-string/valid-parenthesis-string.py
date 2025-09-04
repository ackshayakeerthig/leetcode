class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mini=0
        maxi=0
        for char in s:
            if char=='(':
                mini+=1
                maxi+=1
            if char=='*':
                if mini:
                    mini-=1
                maxi+=1
            if char==')':
                if mini:
                    mini-=1
                if not maxi:
                    return False
                else:
                    maxi-=1
        return mini==0 