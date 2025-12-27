class Solution {
public:
    int jump(vector<int>& nums) {
        int n=nums.size();
        vector<int> dp(n,INT_MAX);
        dp[n-1]=0;
        // calc(nums,dp,n-2);
        for (int i=n-2;i>=0;i--){
            int min=dp[i];
            for (int j=i+1;j<=i+nums[i] && j<n;j++){
                // if (j>=n){
                //     break;
                // }
                if (dp[j]==INT_MAX){
                    continue;
                }
                dp[i]=std::min(dp[i],1+dp[j]);
            }
        }
        return dp[0];
    }
};