class Solution {
    public int stoneGameV(int[] stones) {
        int n=stones.length;
        int prefix[]=new int[n+1];

        for (int i=0;i<n;i++){
            prefix[i+1]=prefix[i]+stones[i];
        }

        int [][] dp=new int[n][n];
        
        for (int l=n-1;l>-1;l--){
            for (int r=0;r<n;r++){
                for (int mid=l;mid<r;mid++){
                    int left_sum=prefix[mid+1]-prefix[l];
                    int right_sum=prefix[r+1]-prefix[mid+1];
                    if (left_sum<right_sum){
                        dp[l][r]=Math.max(dp[l][r],left_sum+dp[l][mid]);
                    }
                    else if (left_sum>right_sum){
                        dp[l][r]=Math.max(dp[l][r],right_sum+dp[mid+1][r]);
                    }
                    else{
                        dp[l][r]=Math.max(dp[l][r],Math.max(right_sum+dp[mid+1][r],left_sum+dp[l][mid]));
                    }
                }
            }
        }
        return dp[0][n-1];
    }
}