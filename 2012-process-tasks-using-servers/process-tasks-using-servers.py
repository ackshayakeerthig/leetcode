class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available_servers=[(weight,index) for index,weight in enumerate(servers)]
        heapq.heapify(available_servers)
        unavailable_servers=[] #(finishtime, weight , index)
        answer=[]
        current_time = 0
        for time,task in enumerate(tasks):
            current_time = max(current_time,time)
            while unavailable_servers and unavailable_servers[0][0]<=time:
                finish,weight,index=heapq.heappop(unavailable_servers)
                heapq.heappush(available_servers,(weight,index))
            # if not available jumping to earliest finish time
            if not available_servers:
                current_time=unavailable_servers[0][0]
                while unavailable_servers and unavailable_servers[0][0]<=current_time:
                    finish,weight,index=heapq.heappop(unavailable_servers)
                    heapq.heappush(available_servers,(weight,index))
            weight,index=heapq.heappop(available_servers)
            answer.append(index)
            heapq.heappush(unavailable_servers,(task+current_time,weight,index))
        return answer