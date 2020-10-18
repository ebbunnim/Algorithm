import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    N = int(input())
    Nlist = [int(input()) for _ in range(N)]
    heapq.heapify(Nlist)
    sumv = 0 # Nlist에 원소 하나면 비교횟수 0 임 주의

    while len(Nlist)!=1:
        tmp=0
        for _ in range(2):
            tmp+=heapq.heappop(Nlist)
        sumv+=tmp
        heapq.heappush(Nlist, tmp)

    print(sumv)