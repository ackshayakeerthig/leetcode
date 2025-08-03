from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        visited = [[0] * cols for _ in range(rows)]
        
        # Mark 'O's connected to boundary as safe using BFS
        for i in range(rows):
            if board[i][0] == 'O':
                self.bfs(board, visited, i, 0)
            if board[i][cols - 1] == 'O':
                self.bfs(board, visited, i, cols - 1)
        
        for j in range(cols):
            if board[0][j] == 'O':
                self.bfs(board, visited, 0, j)
            if board[rows - 1][j] == 'O':
                self.bfs(board, visited, rows - 1, j)
        
        # Now flip unvisited 'O's to 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
    
    def bfs(self, board, visited, row, col):
        q = deque()
        q.append((row, col))
        visited[row][col] = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            cur_row, cur_col = q.popleft()
            for dr, dc in directions:
                nr, nc = cur_row + dr, cur_col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) \
                   and board[nr][nc] == 'O' and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
