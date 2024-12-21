
char ans[10000];
char* revstr(char* str) {
    int len = strlen(str);
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
    return str;
}
char* addBinary(char* a, char* b) {
    int carry=0;
    int n=strlen(a)-1;
    int m=strlen(b)-1;
    int i=n,j=m,p=0;
    while (i>=0 && j>=0){
        if (carry){
            if (a[i]=='1' && b[j]=='1'){
                carry=1;
                ans[p]='1';
            }
            else if (a[i]=='1' || b[j]=='1'){
                carry=1;
                ans[p]='0';
            }
            else{
                carry=0;
                ans[p]='1';
            }
        }
        else {
             if (a[i]=='1' && b[j]=='1'){
                carry=1;
                ans[p]='0';
            }
            else if (a[i]=='1' || b[j]=='1'){
                carry=0;
                ans[p]='1';
            }
            else{
                carry=0;
                ans[p]='0';
            }
        }
        i--;
        j--;
        p++;
    }
    char * cont=(i<0)?b:a;
    int k=(i<0)?j:i;
    while (k>=0){
        if (carry){
            if (cont[k]=='1'){
                ans[p]='0';
                carry=1;
            }
            else{
                ans[p]='1';
                carry=0;
            }
        }
        else{
            carry=0;
            if (cont[k]=='1'){
                ans[p]='1';
            }
            else{
                ans[p]='0';
            }
        }
        k--;
        p++;
    }
    if (carry){
        ans[p]='1';
        p++;
    }
    ans[p]='\0';
    return revstr(ans);
}