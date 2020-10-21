import heapq
# min-heap
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville:
        if len(scoville)<=1:
            break
        if scoville[0]<K:
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            ns = s1 + (s2*2)
            heapq.heappush(scoville,ns)
            cnt += 1
        else:
            break
    if scoville[0]<K:
        return -1
    return cnt