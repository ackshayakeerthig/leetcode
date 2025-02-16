int search(int * nums, int start, int end, int target){
    if (start >end){return end+1;}
    int mid=(start+end)/2;
    if (nums[mid]>target){
        return search(nums,start,mid-1,target);
    }
    else if (nums[mid]<target){
        return search(nums, mid+1,end,target);
    }
    return mid;
}
int searchInsert(int* nums, int numsSize, int target) {
    return search(nums,0,numsSize-1,target);
}