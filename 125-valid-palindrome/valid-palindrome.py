class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=re.sub(r'[^a-z0-9]','',s)
        start=0
        end=len(s)-1
        while (start<end):
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return False
        return True