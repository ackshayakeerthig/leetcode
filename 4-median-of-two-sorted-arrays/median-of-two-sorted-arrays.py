class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        combined=len(A)+len(B)
        isodd=1 if combined%2==1 else 0
        half=combined//2
        if len(A)>len(B):
            B,A=A,B
        left=0
        right=len(A)-1
        while 1:
            i=(left+right)//2
            j=half-(i+1)-1
            aleft=A[i] if i>=0 else float("-infinity")
            aright=A[i+1] if i+1 <len(A) else float("infinity")
            bleft=B[j] if j>=0 else float("-infinity")
            bright=B[j+1] if j+1<len(B) else float("infinity")
            if aleft <= bright and bleft<= aright:
                if isodd:
                    return min(aright,bright)
                else:
                    return  (min(aright,bright)+max(aleft,bleft))/2
            if aleft>bright:
                right-=1
            else:
                left+=1