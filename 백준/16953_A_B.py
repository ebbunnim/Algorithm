import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline
from collections import deque

def mul(a):
    return a*2

def right_add(a):
    return int(str(a)+'1')

def bfs(src):
    Q=deque([(src,1)])
    while Q:
        src,lv=Q.popleft()
        if src==B:
            return lv
        for func in (mul,right_add):
            if 0<=src<=10**9:
                dst=func(src)
                Q.append((dst,lv+1))
    return -1

if __name__ == '__main__':
    A,B=map(int,input().split())
    print(bfs(A))

