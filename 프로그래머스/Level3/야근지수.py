import heapq

def solution(n, works):
    q = [-work for work in works]
    heapq.heapify(q)
    while n != 0:
        n -= 1
        if q:
            x = heapq.heappop(q)
        if x != 0:
            x += 1
            heapq.heappush(q, x)

    return sum([i*i for i in q])