class Solution {
public:
    int find(int i, vector<int> & dp, string s, vector<string>&words, int n){
        if (dp[i]==-1){
            for (string word:words){
                if (s.substr(i,word.size())==word){
                    if(find(i+word.size(),dp,s,words,n)){return dp[i]=1;}
                }
            }
            dp[i]=0;
        }
        return dp[i];
    }
    bool wordBreak(string s, vector<string>& words) {
        int n=s.size();
        vector<int> dp(n+1,-1);
        dp[n]=1;
        return bool(find(0,dp,s,words,n));
    }
};