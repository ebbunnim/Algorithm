import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def must_empty(r,c):
    for i in range(8):
        nr,nc=r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<N:
            if arr[nr][nc]=='0':
                return 1
            if arr[nr][nc]!='#':
                arr[nr][nc]=str(int(arr[nr][nc])-1)
    return 0

if __name__ == '__main__':
    N=int(input())
    arr=[list(input().strip()) for _ in range(N)]
    dr=[-1,-1,-1,0,0,1,1,1]
    dc=[-1,0,1,-1,1,-1,0,1]
    cnt=sum(1 for i in range(N) for j in range(N) if arr[i][j]=='#')
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='#':
                cnt-=must_empty(i,j)
    print(cnt)

