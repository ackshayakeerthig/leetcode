#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int longest=0,maxlen;
    int arr[255]={0};
    int start=0,end=0,i=0,j=0,n=strlen(s);
    for (i=0;i<n;i++){
        maxlen=0;
        for (j=i;j<n;j++){
            if (arr[s[j]]==1){break;}
            arr[s[j]]=1;
            maxlen++;
        }
        for (int k=0;k<255;k++){arr[k]=0;}
        if(maxlen > longest){longest=maxlen;}
        
    }
    return longest;
}