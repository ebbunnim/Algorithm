import sys
from collections import deque
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def bfs(curr):
    global ans
    Q=deque([(curr,0)])
    while Q:
        curr,lv=Q.popleft()
        if lv==K:
            ans=max(ans,int(curr))
            continue
        s=list(curr)
        for i in range(n):
            for j in range(i+1,n):
                s[i],s[j]=s[j],s[i]
                if s[0] == '0':
                    s[i], s[j] = s[j], s[i]
                    continue
                _s = ''.join(s)
                if not cache[int(_s)][lv+1]:
                    cache[int(_s)][lv+1]=True
                    Q.append((_s,lv+1))
                s[i], s[j] = s[j], s[i]

if __name__ == '__main__':
    N,K=input().split()
    K=int(K)
    n=len(N)
    cache = [[False for _ in range(11)] for _ in range(1000001)]
    cache[int(N)][0] = True
    ans=-1
    bfs(N)
    print(ans)
