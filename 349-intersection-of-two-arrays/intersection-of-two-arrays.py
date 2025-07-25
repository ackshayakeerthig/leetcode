class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        unique=[]
        while (i<len(nums1) and j<len(nums2)):
            
            if nums1[i]>nums2[j]:
                j+=1
            elif nums2[j]>nums1[i]:
                i+=1
            else:
                if len(unique)<=0 or unique[-1]!=nums1[i]:
                    unique.append(nums1[i])
                i+=1
                j+=1
        
        return unique
        