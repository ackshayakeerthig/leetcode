class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows=grid.size();
        int cols=grid[0].size();
        queue<vector<int>> q;
        int count=0;
        for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                if (grid[i][j]==2){
                    q.push({i,j});
                }
            }
        }
        vector<vector<int>> adj={{0,1},{0,-1},{1,0},{-1,0}};
        while (!q.empty()){
            int k=q.size();
            for (int i=0;i<k;i++){
                vector<int> current=q.front();
                q.pop();
                for (vector<int> a : adj){
                    int x=current[0]+a[0];
                    int y=current[1]+a[1];
                    if (x>=0 && x <rows && y>=0 && y<cols && grid[x][y]==1){
                        grid[x][y]=2;
                        q.push({x,y});
                    }
                }
            }
            count++;
        }
        for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                if (grid[i][j]==1){
                    return -1;
                }
            }
        }
        if (count==0){
            return count;
        }
        return count-1;
        

    }
};