class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int rows=matrix.length ,cols=matrix[0].length;
        int left,right,up;
        int min=Integer.MAX_VALUE;
        for (int i=1;i<rows;i++){
            for (int j = 0;j<cols;j++){
                if (j>0 && j<cols-1){
                    matrix[i][j]+=Math.min(matrix[i-1][j],Math.min(matrix[i-1][j+1],matrix[i-1][j-1]));
                }
                else if (j==0){
                    matrix[i][j]+=Math.min(matrix[i-1][j],matrix[i-1][j+1]);
                }
                else {
                    matrix[i][j]+=Math.min(matrix[i-1][j],matrix[i-1][j-1]);
                }
                
            }
        }
        min=Integer.MAX_VALUE;
        for (int x : matrix[rows-1]){
            min=Math.min(min,x);
            }
        return min;
        }
    }
