

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
                box=(row//3)*3+col//3
                if digit in rows[row] or digit in cols[col] or digit in boxes[box]:
                    return False
                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box].add(digit)
        return True
                
        