import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def rotate(N, M):
    for i in range(bound):
        # start 잡음
        r, c = i, i
        corners = [(N - 1, i), (N - 1, M - 1), (i, M - 1), (i, i)]
        curr = arr[r][c]
        d = 0
        while True:
            if d == 4:
                break
            nr, nc = r + dr[d], c + dc[d]
            nxt = arr[nr][nc]
            arr[nr][nc] = curr
            r, c = nr, nc
            curr = nxt
            # 방향 턴
            if nr == corners[d][0] and nc == corners[d][1]:
                d += 1
        N -= 1
        M -= 1
    return

if __name__ == '__main__':
    N,M,R=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    bound=min(N,M)//2
    # 반시계방향
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]

    for _ in range(R):
        rotate(N,M)

    for row in arr:
        print(*row)

