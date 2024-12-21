double power(double x, long int n, double ans){
    if (n<0){return 1/power(x,-n,ans);}
    if (n==0){
        return ans;
    }
    if (n%2==1){
        return power(x,n-1,ans*x);
    }
    if (n%2==0){
        return power(x*x,n/2,ans);
    }
    return ans;
}
double myPow(double x, int n) {
    return power(x,n,1);
}