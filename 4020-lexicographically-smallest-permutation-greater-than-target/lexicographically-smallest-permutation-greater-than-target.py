class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        count_chars=[0]*26
        for char in s:
            count_chars[ord(char)-ord('a')]+=1
        def solve(i,greater):
            if i>=len(target):
                return greater
            curchar=target[i]
            for j in range(26):
                if not greater and j<ord(curchar)-ord('a') or count_chars[j]<=0 :
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
        solve(0,False)
        return "".join(cur_str)