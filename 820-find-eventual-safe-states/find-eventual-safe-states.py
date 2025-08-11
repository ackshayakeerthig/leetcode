class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        unsafe=[0]*n
        vis=[0]*n
        pathvis=[0]*n
        def dfs(vertex):
            vis[vertex]=1
            pathvis[vertex]=1
            for adj in graph[vertex]:
                if pathvis[adj]:
                    unsafe[vertex]=1
                    pathvis[vertex]=0
                    return True
                if not vis[adj]:
                    if dfs(adj)==True:
                        unsafe[vertex]=1
                        pathvis[vertex]=0
                        return True
                elif unsafe[adj]:
                        unsafe[vertex]=1
                        pathvis[vertex]=0
                        return True
            pathvis[vertex]=0
            return False
        for i in range(n):
            if not vis[i]:
                dfs(i)
        ans=[]
        for i in range(n):
            if unsafe[i]==0:
                ans.append(i)
        return ans
            

