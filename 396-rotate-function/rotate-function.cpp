class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int summ=accumulate(begin(nums), end(nums), 0);
        int n=nums.size();
        int ans=0;
        vector <int> dp(n,0);
        for (int i=0;i<n;i++){
            dp[0]+=i*nums[i];
        }
        for (int i=1;i<n;i++){
            dp[i]=dp[i-1]+summ -n*nums[n-i];
        }
        return * max_element(begin(dp), end(dp));
    }
};