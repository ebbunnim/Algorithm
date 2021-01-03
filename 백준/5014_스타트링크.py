import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    F,S,G,U,D=map(int,input().split())
    vis=[True]+[False]*F
    def bfs(curr):
        Q=deque([(curr,0)])
        vis[curr]=True
        while Q:
            curr,cnt=Q.popleft()
            if curr==G:
                return cnt
            for delta in (U,-D):
                nxt=curr+delta
                if 0<=nxt<=F and vis[nxt]==False:
                    vis[nxt]=True
                    Q.append((nxt,cnt+1))
    ans=bfs(S)
    if ans is not None:
        print(ans)
    else:
        print("use the stairs")
