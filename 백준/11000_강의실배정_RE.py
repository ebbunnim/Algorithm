import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline
import heapq

if __name__ == '__main__':
    N=int(input())
    heap_for_allocation=[list(map(int,input().split())) for _ in range(N)]
    heapq.heapify(heap_for_allocation)
    fst=heapq.heappop(heap_for_allocation)
    heap_for_validation=[[fst[1],fst[0]]] # 종료 시간 기준
    heapq.heapify(heap_for_validation)
    cnt=1
    while heap_for_allocation:
        cls=heapq.heappop(heap_for_allocation) #(시작,종료)
        top=heap_for_validation[0] #(종료,시작)
        if top[0]<=cls[0]: #replace
            heapq.heappop(heap_for_validation)
        else: #append new cls
            cnt+=1
        heapq.heappush(heap_for_validation, [cls[1], cls[0]])
    print(cnt)
    # 배치 : 하나는 시작 시간 기준으로 강의를 배치한다.
    # 검증 : 다른 하나는, 종료 시간 순으로 가장 이른 애를 top에 배치한다.  (판별하는 녀석)
    # 검증 방법 : 현재 top에 있는 애는 가장 빨리 끝나는 강의. 이것보다 일찍 시작해야 하면 강의실 따로 할당해줘야. 아니라면 강의실 replace하면 됨
    # 1. 할당 - 큐에 넣고 cnt+1
    # 2. replace - 대치할 강의 빼고, 새로운 강의 큐에 넣음











