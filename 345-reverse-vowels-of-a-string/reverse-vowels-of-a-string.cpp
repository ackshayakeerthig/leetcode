class Solution {
public:
    string reverseVowels(string s) {
        int n=s.size(),left=0;
        int right=n-1;
        char temp;
        while (left<right){
            while (left < n && (s[left]!='a' && s[left]!='e' && s[left]!='i'&&s[left]!='o'&&s[left]!='u'&& s[left]!='A' && s[left]!='E' && s[left]!='I'&&s[left]!='O'&&s[left]!='U')){left+=1;}
            while (right > -1 && (s[right]!='a'&& s[right]!='e' && s[right]!='i'&& s[right]!='o'&& s[right]!='u'&& s[right]!='A' && s[right]!='E' && s[right]!='I'&&s[right]!='O'&&s[right]!='U')){right-=1;}
            temp=s[left];
            if (left<right){
                s[left]=s[right];
                s[right]=temp;
                left++;
                right--;}
        }
        return s;
    }
};