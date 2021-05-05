import sys
from collections import deque
sys.stdin = open('input.txt','r')

def bfs(r,c):
    Q=deque()
    Q.append((r,c))
    vis[r][c]=True
    tgts=set()
    while Q:
        r,c=Q.popleft()
        for dirs in D[arr[r][c]]:
            nr,nc=r+dirs[0],c+dirs[1]
            if 0<=nr<N and 0<=nc<M and vis[nr][nc]==False:
                if arr[nr][nc]!='.':
                    vis[nr][nc]=True
                    Q.append((nr, nc))
                else: # 끊긴듯
                    if arr[r][c] == 'M' or arr[r][c] == 'Z': ### 이거 중요. 안하면 반례 틀리고 Name Error 뜬다.
                        continue
                    tgts.add((nr,nc,dirs[0],dirs[1]))
    return tgts

if __name__ == '__main__':
    N,M=map(int,input().split())
    arr=[list(input()) for _ in range(N)]
    vis=[[False]*M for _ in range(N)]
    D={
        'M':[(-1,0),(1,0),(0,-1),(0,1)],
        'Z':[(-1,0),(1,0),(0,-1),(0,1)],
        '|':[(1,0),(-1,0)],
        '-':[(0,1),(0,-1)],
        '+':[(1,0),(-1,0),(0,1),(0,-1)],
        '1':[(0,1),(1,0)],
        '2':[(0,1),(-1,0)],
        '3':[(0,-1),(-1,0)],
        '4':[(0,-1),(1,0)]
    }
    check_list=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='M':
                sr,sc=i,j
            elif arr[i][j]=='Z':
                er,ec=i,j
    remainders=[]
    remainders+=[bfs(sr,sc)]
    remainders+=[bfs(er,ec)]
    for i in range(N):
        for j in range(M):
            if vis[i][j]==False and arr[i][j]!='.':
                remainders+=[bfs(i,j)]
    check=[[0]*M for _ in range(N)]
    for _set in remainders:
        for e in _set:
            check[e[0]][e[1]]+=1
    tgt=[(i,j) for i in range(N) for j in range(M) if check[i][j]>1]
    tr,tc=tgt[0][0],tgt[0][1]
    check_dirs=[]
    for _set in remainders:
        for e in _set:
            if e[0]==tr and e[1]==tc:
                check_dirs+=[(-e[2],-e[3])]
    for key,value in D.items():
        if key in ('M', 'Z'):
            continue
        if sorted(value)==sorted(check_dirs):
            tkey=key
            break
    print(tr+1,tc+1,tkey)




# 방향은 M -> Z 으로 흐른다.
# 방향은 일방향이다.
# 1. 터널 - 방향으로 딕셔너리 구성해야겠다.
# 2. checklist에는 끊겨있는 곳의 방향 정보들을 모두 모은다. 이후 터널 모양을 추론한다.
