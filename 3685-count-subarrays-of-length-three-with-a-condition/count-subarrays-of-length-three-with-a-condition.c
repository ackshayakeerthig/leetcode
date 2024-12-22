int countSubarrays(int* nums, int n) {
    int i=0;
    int count=0;
    for (i=0;i<n-2;i++){
        if ((nums[i]+nums[i+2])*2==nums[i+1]){
            count++;
        }
    }
    return count;
}