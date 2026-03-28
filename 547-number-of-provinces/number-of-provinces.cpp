class Solution {
public:
    void dfs(vector<int>& visited,vector<vector<int>>& isConnected,int i){
        int n=visited.size();
        for (int j=0;j<n;j++){
            if (visited[j]==0 && isConnected[i][j]){
                    visited[j]=1;
                    dfs(visited,isConnected,j);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n=isConnected.size();
        vector<int> visited(n,0);
        int ncomps=0;
        for (int i=0;i<n;i++){
            if (visited[i]==0){
                visited[i]=1;
                ncomps+=1;
                dfs(visited,isConnected,i);
            }
        }
        
        return ncomps;
    }
};