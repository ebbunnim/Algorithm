import sys
sys.stdin = open('input.txt','r')
import heapq
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    min_heap=[]
    max_heap=[]
    # init
    initial=int(input())
    print(initial)
    heapq.heappush(max_heap,-initial)
    for i in range(1,N):
        if i%2:
            heapq.heappush(min_heap,int(input()))
        else:
            heapq.heappush(max_heap,-int(input()))
        if min_heap[0] < -max_heap[0]:
            min_top=heapq.heappop(min_heap)
            max_top=-heapq.heappop(max_heap)
            heapq.heappush(min_heap,max_top)
            heapq.heappush(max_heap,-min_top)
        print(-max_heap[0])
