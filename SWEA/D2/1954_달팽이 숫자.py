import sys
sys.stdin = open('input.txt','r')


dx = [0,1,0,-1] #우하좌상
dy = [1,0,-1,0]

if __name__=="__main__":
    for t in range(int(input())):
        N = int(input())
        arr = [[0]*N for _ in range(N)]
        num=1
        target = N*N

        direction = 0
        x, y = 0, 0
        arr[0][0]=1

        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]==0:
                num+=1
                x = nx
                y = ny
                arr[nx][ny]=num
            else: # 인덱스 초과했거나 방문처리한 곳 다시 되돌아오면
                direction=(direction+1)%4

            if num == target:
                break
        print(f'#{t+1}')
        for i in range(N):
            for j in range(N):
                print(arr[i][j],end=' ')
            print()
