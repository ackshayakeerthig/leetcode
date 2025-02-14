char* longestCommonPrefix(char** str, int size) {
    char * arr=(char *)malloc(200);
    int i=0;
    int k=0;
    while (str[0][i]!=0){
        for (int j =0;j<size;j++){
            
            if (str[j][i]!=str[0][i]){
                arr[k]=0;
                return arr;
            }
        
        }
        arr[k++]=str[0][i];
        i++;
    }
    arr[k]=0;
    return arr;
}