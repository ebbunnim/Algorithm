import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline
import heapq
from collections import deque

if __name__ == '__main__':
    N=int(input())
    Q=[list(map(int,input().split())) for _ in range(N)]
    Q.sort()
    Q=deque(Q)
    heap=[]
    curr=Q.popleft()
    heapq.heappush(heap,[curr[1],curr[0]]) # 종료시간 빠른 순
    cnt=1
    while Q:
        curr=heapq.heappop(heap)
        nxt=Q.popleft()
        # if -curr[0]<=nxt[0]: # replace (현재 들어있는 종료시간보다 다음 강의 시작시간이 같거나 크다면,)
        #     heapq.heappush(heap,[-nxt[1],nxt[0]])
        if curr[0]>nxt[0]:
        # append
            heapq.heappush(heap,curr)
            cnt+=1
        heapq.heappush(heap, [nxt[1], nxt[0]])


    print(cnt)











