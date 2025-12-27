class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size();
        vector<bool> dp(n,false);
        dp[n-1]=true;
        // calc(nums,dp,n-2);
        for (int i=n-2;i>=0;i--){
            for (int j=i+1;j<=i+nums[i];j++){
                if (j>=n){
                    break;
                }
                if (dp[j]==true){
                    dp[i]= true;
                    break;
                }
            }
        }
        return dp[0];
    }
    // bool calc(vector<int>& nums, vector<bool> & dp, int i){
    //     if (i<0){
    //         return ;
    //     }
    //     for (int j=0;j<=nums[i];j++){
    //         if (j>=nums.size()){
    //             break;
    //         }
    //         if (dp[j]==true){
    //             dp[i]=true;
    //             break;
    //         }
    //     }
    // }
};