import sys
sys.stdin = open('input.txt','r')

import heapq
from collections import deque

if __name__ == '__main__':
    N, K= map(int, input().split())
    jewelry = [list(map(int,input().split())) for _ in range(N)]
    jewelry.sort()
    jewelry = deque(jewelry)
    bags = [int(input()) for _ in range(K)]
    bags.sort()

    heap=[]
    sumv=0

    for i in range(K):
        while jewelry:
            if bags[i]>=jewelry[0][0]:
                jewel = jewelry.popleft()
                heapq.heappush(heap, (-jewel[1],jewel[0]))
            else:
                break
        if heap:
            sumv += abs(heapq.heappop(heap)[0])

    print(sumv)

    # 가장 가벼운 가방부터, 이 가방에 들어갈 수 있는 모든 보석들을 다 넣어 둔다.
    # 가장 큰 가치를 가진 보석을 빼기 위해 max-heap을 구성했다.
    # 한 가방씩, 그 가방에 들어갈 수 있는 보석중 최대 가치를 가진 보석이 heap의 top에 위치해있다. 이걸 빼준다.
    # 다음 번 순회도 마찬가지다. 다만, heap에는 앞선 '더 가벼운' 가방에 들어갈 수 있는 보석들이 위치해 있어서, 만약 다음 번에 무게가 더 나가지만 가치가 적은 보석이 들어오더라도 max-heap에서는 최대 가치의 보석을 보장한다.


    # 아래처럼 하면, 특정 가방에 대해서 제일 비싼 보석을 캐치할 수 없음. 전체 가능한 케이스들이 다 들어가므로
    # sumv = 0
    # for _ in range(K):
    #     if heap:
    #         sumv+= abs(heapq.heappop(heap)[0])
    #
