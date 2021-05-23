# 작업 스케줄링, 우선순위큐
import heapq

def solution(t, r):
    answer = []
    heap=[]
    sort_list = [(v,i) for i,v in enumerate(t)] # lift_id, customer_id
    sort_list.sort(reverse=True)
    start_t,finish_t=0,max(t)
    while start_t!=finish_t+1:
        while sort_list and sort_list[-1][0]==start_t:
            lift_id,customer_id=sort_list.pop()
            heapq.heappush(heap,(r[customer_id],lift_id,customer_id))
        start_t+=1
        if heap:
            _, _, customer_id = heapq.heappop(heap)
            answer+=[customer_id]
    while heap: # for left customers
        _, _, customer_id = heapq.heappop(heap)
        answer+=[customer_id]
    return answer

print(solution([0,1,3,0],[0,1,2,3]))
