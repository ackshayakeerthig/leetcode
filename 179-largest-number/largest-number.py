class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        result="".join(nums)
        if result[0]=='0':
            return "0"
        return result
        