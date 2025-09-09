class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        left=0
        right=0
        maxi=0
        for char in s:
            if char=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxi=max(maxi, 2*left)
            elif left<right:
                left=0
                right=0
        maxi2=0
        left=0
        right=0
        for i in range(n-1,-1,-1):
            if s[i]==')':
                right+=1
            else:
                left+=1
            if right==left:
                maxi2=max(right*2,maxi2)
            elif right<left:
                right=0
                left=0
        return max(maxi,maxi2)