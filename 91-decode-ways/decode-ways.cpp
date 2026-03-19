class Solution {
public:
    int numDecodings(string s) {
        int n=s.size();
        vector<int> dp(n,-1);
        return find(0,dp,s);
    }
    int find(int i, vector<int>&dp,string&s){
        if (i==s.size()){
            return 1;
            }
        if (dp[i]==-1){
            dp[i]=0;
            if (s[i]>='1' and s[i]<='9'){
                dp[i]+=find(i+1,dp,s);
            }
            if (i+1 < s.size() && stoi(s.substr(i,2))>=10 && stoi(s.substr(i,2))<=26){
                dp[i]+=find(i+2,dp,s);
            }
        }
        return dp[i];
    }
};