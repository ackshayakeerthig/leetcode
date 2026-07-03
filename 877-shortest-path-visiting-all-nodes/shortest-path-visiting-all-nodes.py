from queue import Queue
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        visited=set()
        q=deque()
        for i in range(n):
            q.append((i, 1<<i))
            visited.add((i, 1<<i))
        path=0
        all_visited_mask=(1<<n)-1
        while q:
            # print(q,path)
            for i in range(len(q)):
                cur_node,cur_mask=q.popleft()
                if cur_mask==all_visited_mask:
                    return path
                for next_node in graph[cur_node]:
                    next_mask=cur_mask | 1<<next_node
                    if (next_node,next_mask) not in visited:
                        q.append((next_node,next_mask))
                        visited.add((next_node,next_mask))
            path+=1
        return path