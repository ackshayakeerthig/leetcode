class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_cnt=0
        even_cnt=0
        mini=float('inf')
        for num in nums1:
            if num%2:
                odd_cnt+=1
            else :
                even_cnt+=1
            mini=min(mini,num)
        if odd_cnt==len(nums1) or even_cnt==len(nums1):
            return True
        if mini%2==1:
            return True
        return False