def solve(board:list,rows:list,cols:list,boxes:list,empty_places:list):
    if (len(empty_places)==0):
        return True
    for place in range(0,len(empty_places)):
        row,col=empty_places[place]
        for digit in range(1,10):
            digit=str(digit)
            box=(row//3)*3+col//3
            if not(digit in rows[row] or digit in cols[col] or digit in boxes[box]):
                board[row][col]=digit
                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box].add(digit)
                if (solve(board,rows,cols,boxes,empty_places[place+1:])):
                    return True
                else:
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    boxes[box].remove(digit)
        return False


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set([]) for i in range(0,9)]
        cols=[set([]) for i in range(0,9)]
        boxes=[set([]) for i in range(0,9)]
        empty_places=[]
        for row in range(0,9):
            for col in range(0,9):
                digit=board[row][col]
                if digit=='.': 
                    empty_places.append((row,col))
                    continue
                box=(row//3)*3+col//3
                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box].add(digit)
        solve(board,rows,cols,boxes,empty_places)
        