import sys
import heapq
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=[list(map(int,input().split())) for _ in range(N)]
    Nlist.sort() # 배치 : 순차적
    heap=[]
    for deadline,val in Nlist:
        if deadline<=len(heap): # 검증 : heap의 length(할당할 수 있는 숙제 수)는 데드라인보다는 항상 작거나 같아야 한다.
            heapq.heappop(heap)
        heapq.heappush(heap,val)
    print(sum(heap))

