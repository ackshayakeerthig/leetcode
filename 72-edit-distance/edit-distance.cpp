class Solution {
public:
    int minDistance(string word1, string word2) {
        int m=word1.size();
        int n=word2.size();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return find(m-1,n-1,dp,word1,word2);
        }
        
    int find(int i, int j, vector<vector<int>>& dp, string & word1, string & word2){
        if (i<0){
            return j+1;
        }
        if (j<0){
            return i+1;

        }
        if (dp[i][j]==-1){
            if (word1[i]==word2[j]){
                dp[i][j]=find(i-1,j-1,dp,word1,word2);
            }
            else{
                dp[i][j]=1+std::min({find(i-1,j-1,dp,word1,word2),find(i,j-1,dp,word1,word2),find(i-1,j,dp,word1,word2)});
            }
        }
        return dp[i][j];
    }
};