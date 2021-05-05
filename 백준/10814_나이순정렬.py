import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline
import heapq
if __name__=="__main__":
    N=int(input())
    heap=[]
    for i in range(N):
        age,name=input().strip().split()
        heapq.heappush(heap,(int(age),i,name))
    while heap:
        age,_,name = heapq.heappop(heap)
        print(age,name)




