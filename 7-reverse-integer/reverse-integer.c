int revans(int x, int ans){
    if (x==0){return ans;}
    if (ans > INT_MAX / 10 || (ans == INT_MAX / 10 && x % 10 > 7)) return 0;
    if (ans < INT_MIN / 10 || (ans == INT_MIN / 10 && x % 10 < -8)) return 0;
    return revans(x/10,x%10+ans*10);
}
int reverse(int x){
    // if (x==pow(2,31)){return 0;}
    return revans(x,0);
}