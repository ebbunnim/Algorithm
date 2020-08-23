import sys
sys.stdin = open("input.txt", "r")

def notwall(x, y):
    return 0<=x<N and 0<=y<N and arr[y][x]!=1


# 모든 이동가능한 경우의 수를 구하기 (재귀의 종료조건은 x, y모두 N으로 되었을 때)
def DFS(x, y):
    global cnt
    if x==N-1 and y==N-1:
        cnt += 1
        return
    visited[x][y] = 1
    for i in range(3):
        new_x=x+delta[i][1]
        new_y=y+delta[i][0]
        if notwall(new_x, new_y) and visited[new_x][new_y] != 1:
            visited[new_x][new_y]=1
            if i==1: # 대각선으로 들어왔을때,
                visited[new_x-1][new_y]=1
                visited[new_x][new_y-1]=1
                DFS(new_x, new_y)
                # visited[new_x-1][new_y]=0
                # visited[new_x][new_y-1]=0
            DFS(new_x, new_y)
            visited[new_x][new_y]=0
        else: # 원래라면 그냥 return 만 하면 되는데, 처음 들어왔을때 아예 길이 없으면 0으로 빠져라가 의도
            return 0


if __name__=="__main__":
    N=int(input())
    arr=[0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    visited=[[0]*N for _ in range(N)]
    print(*arr, sep='\n')
    # index를 1부터 N까지 잡음 주의하기
    # (열, 행) 순으로
    delta=[(0,1),(1,1),(1,0)]
    cnt=0
    DFS(0,0)
    # visited[0][0]=1
    print(cnt)
