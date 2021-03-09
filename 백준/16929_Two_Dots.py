import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def is_cycle(r,c,sr,sc,color,cnt):
    for i in range(4):
        nr,nc=r+dr[i],c+dc[i]
        if (nr, nc) == (sr, sc) and cnt >= 4:
            return True
        if 0<=nr<N and 0<=nc<M and not vis[nr][nc] and color==board[nr][nc]:
            vis[nr][nc] = True
            if is_cycle(nr,nc,sr,sc,color,cnt+1):
                return True
            vis[nr][nc] = False

if __name__ == '__main__':
    N,M=map(int,input().split())
    board=[input().strip() for _ in range(N)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    vis=[[False]*M for _ in range(N)]
    ans='No'
    for i in range(N):
        for j in range(M):
            if not vis[i][j]:
                vis[i][j]=True
                if is_cycle(i,j,i,j,board[i][j],1):
                    ans='Yes'
                    break
        if ans=='Yes':
            break
    print(ans)
