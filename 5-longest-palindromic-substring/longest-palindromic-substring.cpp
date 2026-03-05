class Solution {
    
public:
    int find(std::vector<std::vector<int>>& dp, string& s, int i, int j) {
        if (i >= j)  return 1;
        if (dp[i][j]!=-1){
            return dp[i][j];
        }
        dp[i][j]=find(dp,s,i+1,j-1)&& (s[i]==s[j]);
        return dp[i][j];
    }
    string longestPalindrome(string s) {
        int n=s.size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, -1));
        
        int start=0, maxlen=1;
        int len=maxlen;
        for (int i=0;i<n;i++){
            dp[i][i]=1;
        }
        for (int i=0;i<n-1;i++){
            dp[i][i+1]=(s[i]==s[i+1])?1:0;
            if (dp[i][i+1]==1){
                start=i;
                maxlen=2;
            }
        }
        for (int i=0;i<n;i++){
            for (int j=i+2;j<n;j++){
                if (find(dp,s,i,j)==1){
                    len=j-i+1;
                    if (len>maxlen){
                        start=i;
                        maxlen=len;
                    }
                }
            }
        }
        return s.substr(start,maxlen);
    }
};