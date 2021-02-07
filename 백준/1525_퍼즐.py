import sys
from collections import deque,defaultdict
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def bfs():
    while Q:
        s=Q.popleft()
        if s=='123456780':
            return D[s]
        zero=s.find('0')
        r,c=zero//3,zero%3
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            s_list=list(s)
            if 0<=nr<3 and 0<=nc<3:
                nzero=3*nr+nc
                s_list[nzero],s_list[zero]=s_list[zero],s_list[nzero] # swap
                res=''.join(s_list)
                if not D[res]:
                    D[res]=D[s]+1
                    Q.append(res)
    return -1

if __name__ == '__main__':
    arr=[input().strip().split() for _ in range(3)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    D=defaultdict(int)
    s=''
    for i in range(3):
        s+=''.join(arr[i])
    Q=deque([s])
    print(bfs())