class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev=0
        for x in s.split():
            if x.isdigit() :
                if int(x)<=prev:
                    return False
                prev=int(x)
        return True