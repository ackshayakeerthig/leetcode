class Solution {
public:
    int balancedStringSplit(string s) {
        int total=0;
        int cnt=0;
        for (int i=0;i<s.size();i++){
            if (s[i]=='R'){
                cnt+=1;
            }
            else{
                cnt-=1;
            }
            if (cnt==0){
                total+=1;
            }
        }
        return total;
    }
};