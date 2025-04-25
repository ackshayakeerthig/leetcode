def findbox(row :int ,col:int)->int:
    boxrow=row//3
    boxcol=col//3
    if boxrow==0:
        if boxcol==0:
            return 0
        elif boxcol==1:
            return 1
        return 2
    elif boxrow==1:
        if boxcol==0:
            return 3
        elif boxcol==1:
            return 4
        return 5
    if boxcol==0:
            return 6
    elif boxcol==1:
            return 7
    return 8

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set([]) for i in range(0,9)]
        cols=[set([]) for i in range(0,9)]
        boxes=[set([]) for i in range(0,9)]
        for row in range(0,9):
            for col in range(0,9):
                digit=board[row][col]
                if digit=='.':
                    continue
                if digit in rows[row]:
                    return False
                else :
                    rows[row].add(digit)
                if digit in cols[col]:
                    return False
                else :
                    cols[col].add(digit)
                    box=findbox(row,col)
                    if digit in boxes[box]:
                       return False
                    else :
                      boxes[box].add(digit)
        return True
                
        