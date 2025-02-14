int mySqrt(int x) {
    int j=0;
    for (long int i=0;i*i<=x;i++){
        j=i;
    }
    return j;
}