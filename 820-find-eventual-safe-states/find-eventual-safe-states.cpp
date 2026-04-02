class Solution {
public:

    bool dfs(vector<vector<int>>& graph,vector<int>& visited,vector<int> & inrecursion,vector<int>& safe, int current_node){
        if (safe[current_node]!=-1){
            return safe[current_node];
        }
        vector<int>& neighbours=graph[current_node];
        visited[current_node]=1;
        if (neighbours.size()==0){
            safe[current_node]=1;
            return true;
        }
        inrecursion[current_node]=1;
        for (int neighbour : neighbours){
            if (!visited[neighbour]){
                if (dfs(graph,visited,inrecursion,safe,neighbour)==false){
                    safe[current_node]=0;
                    return false;
                }
            }
            else if (inrecursion[neighbour]){
                safe[current_node]=0;
                return false;
            }
        }
        inrecursion[current_node]=0;
        safe[current_node]=1;
        return true;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> safe(n,-1);
        vector<int> visited(n,0);
        vector<int> inrecursion(n,0);
        for (int i=0;i<n;i++){
            if (visited[i]==0){
                dfs(graph,visited,inrecursion,safe,i);
            }
        }
        vector<int> result;
        for (int i=0;i<n;i++){
            if (safe[i]==1){
                result.push_back(i);
            }
        }
        return result;

    }
};