class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        pattern=""
        i=0
        self.patterns(l,pattern,2*n,i)
        return l
    def validity(self,pattern:str,n:int):
        stack=[]
        for i in range(len(pattern)):
            if pattern[i]=="(":
                stack.append(pattern[i])
            else:
                if len(stack)<=0 or  stack.pop()!="(":
                    return False
        if len(pattern)<n:
            return True
        if len(stack)==0:
            return True
        return False

    def patterns(self, l:list ,pattern:str ,n:int, i:int):
        if i>=n:
            l.append(pattern)
            # for pat in l:
            #     if validity()
            return
        pattern=pattern+"("
        if self.validity(pattern, n):
            self.patterns(l,pattern,n,i+1)
        pattern=pattern[:-1]
        pattern=pattern+")"
        if self.validity(pattern, n):
            self.patterns(l,pattern,n,i+1)
        pattern=pattern[:-1]
        return
        
        