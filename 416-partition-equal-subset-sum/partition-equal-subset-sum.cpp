class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum=std::accumulate(nums.begin(),nums.end(),0);
        if (sum%2==1){
            return false;
        }
        sum/=2;
        int n=nums.size();
        vector<vector<int>> dp(n+1, vector<int>(sum+1, false));
        for (int i=0;i<=n;i++){
            dp[i][0]=true;
        }
        for (int i=1;i<=n;i++){
            for (int j=1;j<=sum;j++){
                bool take=false;
                bool not_take=dp[i-1][j];
                if (j>=nums[i-1]){
                    take=dp[i-1][j-nums[i-1]];
                }
                dp[i][j]=take || not_take;
            }
        }
        // return funct(nums,sum, 0, 0,dp);
        return dp[n][sum];
    }
private:
    bool funct(vector<int>& nums, int sum, int temp, int i,vector<vector<int>> & dp){
        if (temp==sum){return true;}
        if (i>=nums.size() || temp>sum){
            return false;
        }
        if (dp[i][temp]!=-1){return dp[i][temp];}
        else{
            bool take=false;
            bool not_take=funct(nums, sum, temp, i+1,dp);
            take=funct(nums,sum, temp+nums[i],i+1,dp);
            dp[i][temp]= take || not_take;
        }
        return dp[i][temp];
    }
};