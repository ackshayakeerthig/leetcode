class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1
        width=0
        for char in s:
            pixels=widths[ord(char)-ord('a')]
            if width+pixels>100:
                lines+=1
                width=pixels
            else:
                width+=pixels
        return [lines,width]