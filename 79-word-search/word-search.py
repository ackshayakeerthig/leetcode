class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visited=[[0]*cols for _ in range(rows)]
        def dfs(cur_i,cur_j,word_pos):
            if not (0<=cur_i<rows and 0<=cur_j<cols) or visited[cur_i][cur_j]:
                return False
            if board[cur_i][cur_j]!=word[word_pos]:
                return False
            if word_pos==len(word)-1:
                return True
            visited[cur_i][cur_j]=1
            found= dfs(cur_i+1,cur_j,word_pos+1) or dfs(cur_i,cur_j+1,word_pos+1) or dfs(cur_i-1,cur_j,word_pos+1) or dfs(cur_i,cur_j-1,word_pos+1)
            visited[cur_i][cur_j]=0        
            return found
        for i in range(rows):
            for j in range(cols):
                visited=[[0]*cols for _ in range(rows)]
                if dfs(i,j,0):
                    return True
        return False
