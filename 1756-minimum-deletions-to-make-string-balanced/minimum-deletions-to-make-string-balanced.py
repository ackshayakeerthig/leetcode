class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a,total_b=s.count('a'),s.count('b')
        left_a=0
        left_b=0
        right_a=total_a
        right_b=total_b
        todelete=len(s)
        for char in s:
            todelete=min(left_b+right_a,todelete)
            if char=='a':
                left_a+=1
                right_a-=1
            if char=='b':
                left_b+=1
                right_b-=1
        todelete=min(left_b+right_a,todelete)    
        return todelete