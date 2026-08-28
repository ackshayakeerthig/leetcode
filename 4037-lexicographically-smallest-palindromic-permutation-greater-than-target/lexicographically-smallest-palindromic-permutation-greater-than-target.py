class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count_chars=[0]*26
        for char in s:
            count_chars[ord(char)-ord('a')]+=1
        middle_char=None
        for i in range(26):
            if count_chars[i]%2==0:
                count_chars[i]//=2
            elif not middle_char:
                middle_char=chr(i+ord('a'))
                count_chars[i]=(count_chars[i]+1)//2
            else:
                return ""
        def solve(i,greater):
            if i>=len(target)//2:
                if greater:
                    return True
                ans="".join(cur_str)
                if middle_char:
                    return ans+middle_char+ans[::-1]>target
                return ans+ans[::-1]>target
            curchar=target[i]
            for j in range(26):
                if not greater and j<ord(curchar)-ord('a') or count_chars[j]<=0 or middle_char and j==ord(middle_char)-ord('a') and count_chars[j]==1:
                    continue
                
                cur_str.append(chr(j+ord('a')))
                count_chars[j]-=1
                greater=greater or j>ord(curchar)-ord('a')
                if solve(i+1,greater):
                    return True
                
                cur_str.pop()
                count_chars[j]+=1
            return False
        cur_str=[]
        if not solve(0,False):
            return ""
        answer= "".join(cur_str)
        if middle_char:
            return answer+middle_char+answer[::-1]
        return answer+answer[::-1]