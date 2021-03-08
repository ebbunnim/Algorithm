import sys
sys.stdin = open('input.txt','r')
from collections import deque
input=sys.stdin.readline

def bfs():
    Q=deque([(1,0)])
    vis[1]=True
    while Q:
        src,lv=Q.popleft()
        if src==100:
            print(lv)
            return
        for delta in range(1,7):
            dst=src+delta
            if 1<=dst<=100:
                if ladder_or_snake[dst]:
                    dst = ladder_or_snake[dst]
                if 1<=dst<=100 and not vis[dst]:
                    vis[dst]=True
                    Q.append((dst,lv+1))
    return

if __name__ == '__main__':
    N,M = map(int, input().split())
    vis=[False]*101
    ladder_or_snake=[0]*101
    for _ in range(N+M):
        a,b=map(int,input().split())
        ladder_or_snake[a]=b
    bfs()