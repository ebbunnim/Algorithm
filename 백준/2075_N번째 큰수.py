import sys
sys.stdin = open('input.txt','r')

import heapq
if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    idx = 0
    for e in arr[N-1]:
        heapq.heappush(heap,(-e,e,N-1,idx)) # 우선순위, 값, 행, 열
        idx += 1

    # pop하면 그 원소의 바로 윗 행 원소를 가져오겠다.
    for i in range(N):
        if i == N-1:
            print(heapq.heappop(heap)[1])
            break
        p, v, r, c = heapq.heappop(heap)
        heapq.heappush(heap, (-arr[r-1][c],arr[r-1][c], r-1, c))
