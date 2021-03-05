import sys
sys.stdin = open('input.txt','r')
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N,K=map(int,input().split())
    Q=deque()
    vis=[False]*100001
    def bfs():
        Q=deque([(N,0)])
        vis[N]=True
        while Q:
            x,t=Q.popleft()
            if x==K:
                print(t)
                return
            if 0<=x-1<=100000 and not vis[x-1]:
                vis[x-1]=True
                Q.append((x-1,t+1))
            if 0<=x+1<=100000 and not vis[x+1]:
                vis[x+1]=True
                Q.append((x+1,t+1))
            if 0<=2*x<=100000 and not vis[2*x]:
                vis[2*x]=True
                Q.append((2*x,t+1))
    bfs()