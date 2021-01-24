import sys
from collections import deque
input=sys.stdin.readline

def push(window,i):
    while window and window[-1][1]>=Nlist[i]:
        window.pop()
    window.append((i,Nlist[i]))

if __name__ == '__main__':
    N,L=map(int,input().split())
    Nlist=list(map(int,input().split()))

    # initial window
    window=deque()
    for i in range(L):
        push(window,i)
        print(window[0][1],end=' ')

    for i in range(L,N):
        if window[0][0]+L<=i:
            window.popleft()
        push(window,i)
        print(window[0][1],end=' ')
