import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def rotate(i,R):
    for _ in range(R): # rotate 횟수
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
            if nr == corners[d][0] and nc == corners[d][1]:
                d += 1

if __name__ == '__main__':
    N,M,R=map(int,input().split())
    cycle=(N-1)*2+(M-1)*2 # 테두리 길이
    arr=[list(map(int,input().split())) for _ in range(N)]
    bound=min(N,M)//2
    # 반시계방향
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]

    for i in range(bound): # 각각의 테두리
        rotate(i,R%cycle) # 가장 바깥 -> 안쪽 -> 안쪽... 으로 각각 회전. 단, 회전 횟수는 테두리 길이에 따라 다르다.
        N-=1
        M-=1
        cycle-=8

    for row in arr:
        print(*row)


