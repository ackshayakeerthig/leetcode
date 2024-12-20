int reverse(long int x,long int ans){
    if (x==0){
        return ans;
    }
    return reverse(x/10,ans*10+x%10);
}
bool isPalindrome(long int x) {
    if (x<0){
        return 0;
    }
    return reverse(x,0)==x;
}