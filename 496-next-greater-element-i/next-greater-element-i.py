class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums2)
        d={}
        nextg=[0]*n
        stack=[nums2[n-1]]
        # nextg[n-1]=-1
        d[nums2[n-1]]=-1
        for i in range(n-2,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            # nextg[i]=stack[-1] if stack else -1
            d[nums2[i]]=stack[-1] if stack else -1
            stack.append(nums2[i])
        result=[]
        for num in nums1:
            # for i in range(n):
            #     if num==nums2[i]:
            #         result.append(nextg[i])
            if num in d:
                result.append(d[num])
        return result


        
        