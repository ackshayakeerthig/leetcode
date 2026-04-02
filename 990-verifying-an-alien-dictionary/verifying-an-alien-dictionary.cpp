class Solution {
public:
    bool issorted(string & small, string & large,vector<int> & rank){
        for (int i=0;i<min(small.size(),large.size());i++){
            if (rank[small[i]-'a'] < rank[large[i]-'a']) return true;
            if (rank[small[i]-'a'] > rank[large[i]-'a']) return false;
        }
        return small.size() <= large.size();
    }
    bool isAlienSorted(vector<string>& words, string order) {
        int n=words.size();
        vector<int> rank(26);
        for (int i=0;i<26;i++){
            rank[order[i]-'a']=i;
        }
        for (int i=0;i<n-1;i++){
            if (issorted(words[i],words[i+1],rank)==false){
                return false;
            }
        }
        return true;
    }
};