import sys
sys.stdin = open('input.txt','r')

def dfs(r,c,lv):
    global ans
    ans=max(ans,lv)
    for i in range(4):
        nr,nc=r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and not vis[ord(arr[nr][nc])-65]:
            vis[ord(arr[nr][nc])-65]=True
            dfs(nr,nc,lv+1)
            vis[ord(arr[nr][nc])-65]=False
    return

if __name__ == '__main__':
    N,M=map(int,input().split())
    arr=[list(input()) for _ in range(N)]
    vis=[False]*26
    ans=0
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    vis[ord(arr[0][0])-65]=True
    dfs(0,0,1)
    print(ans)