class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n=fruits.size();
        int l=0,r=0,maxlen=0;
        unordered_map <int,int> last_seen;
        while (r<n){
            last_seen[fruits[r]]=r;
            if (last_seen.size()>2){
                int minIndex=n;
                int remove=-1;
                for (auto&p: last_seen){
                    if (p.second<minIndex){
                        minIndex=p.second;
                        remove=p.first;
                    }
                }
                last_seen.erase(remove);
                l=minIndex+1;
            }
            maxlen=max(r-l+1,maxlen);
            r++;
        }
        return maxlen;
    }
};