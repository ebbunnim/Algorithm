from collections import deque

def D(num):
    return ((num*2)%10000,'D')

def S(num):
    if num==0:
        return (9999,'S')
    return (num-1,'S')

def L(num):
    q=num//1000
    return ((num-q*1000)*10+q,'L')

def R(num):
    r=num%10
    return ((num-r)//10+(r*1000),'R')

def bfs():
    Q = deque([(start, '')])
    vis[start] = True
    while Q:
        curr, res = Q.popleft()
        if curr == end:
            return res
        for nxt in D(curr), S(curr), L(curr), R(curr):
            if vis[nxt[0]] == False:
                vis[nxt[0]] = True
                Q.append((nxt[0], res + nxt[1]))
    return

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        start,end = map(int,input().split())
        vis = [False] * 10000
        print(bfs())
