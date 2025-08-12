class Solution {
public:
    int mySqrt(int x) {
        long low=1,high=x;
        long mid,sq;
        while (low<=high){
            mid=(low+high)/2;
            sq=mid*mid;
            if (sq==x){
                return mid;
            }
            else if (sq>x){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return high;
    }
};