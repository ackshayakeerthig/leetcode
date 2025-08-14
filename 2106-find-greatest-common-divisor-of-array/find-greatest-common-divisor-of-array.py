class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        if mini==0:
            return maxi
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        return gcd(maxi,mini)