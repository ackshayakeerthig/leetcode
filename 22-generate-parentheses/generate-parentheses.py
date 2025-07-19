class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        pattern=""
        i=0
        self.patterns(l,pattern,2*n,0,0)
        return l
    def validity(self,pattern:str,n:int):
        stack=[]
        for i in range(len(pattern)):
            if pattern[i]=="(":
                stack.append(pattern[i])
            else:
                if len(stack)<=0 or  stack.pop()!="(":
                    return False
        if len(pattern)<=n/2:
            return True
        elif len(pattern)>n/2 and len(pattern)<n:
            if pattern.count("(")>n/2:
                return False
            else:
                return True
        if len(stack)==0:
            return True
        return False

    def patterns(self, l:list ,pattern:str ,n:int, open,close):
        if len(pattern)>=n:
            l.append(pattern)
            return
        if open<n/2:
            self.patterns(l,pattern+'(',n,open+1,close)
        if close<open:
            self.patterns(l,pattern+')',n,open,close+1)
        return
        
        