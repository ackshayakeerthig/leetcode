int priority(char ch){
    if (ch=='I')
       return 1;
     if (ch=='V')
       return 2;
     if (ch=='X')
       return 3;
     if (ch=='L')
       return 4;
     if (ch=='C')
       return 5;
     if (ch=='D')
       return 6;
     if (ch=='M')
       return 7;
    return 0;
}
int romanToInt(char* s) {
    int sum=0;
    int i=0;
    for (i=0;i<strlen(s);i++){
        switch(s[i]){
            case 'I':
               if (priority(s[i])<priority(s[i+1])){
                sum-=1;}
               else{
                sum+=1;
               }
               break;
            case 'V':
               if (priority(s[i])<priority(s[i+1])){
                sum-=5;}
               else{
                sum+=5;
               }
               break;
            case 'X':
               if (priority(s[i])<priority(s[i+1])){
                sum-=10;}
               else{
                sum+=10;
               }
               break;
            case 'L':
               if (priority(s[i])<priority(s[i+1])){
                sum-=50;}
               else{
                sum+=50;
               }
               break;
            case 'C':
               if (priority(s[i])<priority(s[i+1])){
                sum-=100;}
               else{
                sum+=100;
               }
               break;
            case 'D':
               if (priority(s[i])<priority(s[i+1])){
                sum-=500;}
               else{
                sum+=500;
               }
               break;
            case 'M':
               if (priority(s[i])<priority(s[i+1])){
                sum-=1000;}
               else{
                sum+=1000;
               }
               break;
               }
        }
        return sum;
    }
    
