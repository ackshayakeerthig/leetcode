class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int rows=matrix.size();
        int cols=matrix[0].size();
        for (int i=1;i<rows;i++){
            for (int j=0;j<cols;j++){
                if (j>0 and j<cols-1){
                    matrix[i][j]+=min({matrix[i-1][j],matrix[i-1][j+1],matrix[i-1][j-1]});
                }
                else if (j==0){
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1]);
                }
                else if (j==cols-1){
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1]);
                }
                else{
                    matrix[i][j]+=matrix[i-1][j];
                }
            }
        }
        return *min_element(matrix[rows-1].begin(), matrix[rows-1].end());
    }
};