from collections import deque

def bfs():
    Q.append((r1,c1))
    vis[r1][c1] = True
    cnt = 0
    while Q:
        # cnt와 for _ in range(len(Q))의 위치가 이래야 계층적 위치를 잘 알 수 있다.
        cnt+=1
        for _ in range(len(Q)):
            r,c = Q.popleft()
            for a, b in dirs:
                # 새롭게 움직인 방향
                nr = r + a
                nc = c + b
                if nr == r2 and nc == c2:
                    return cnt
                if 0<=nr<N and 0<=nc<N and vis[nr][nc] == False:
                    vis[nr][nc] = True
                    Q.append((nr,nc))

    return -1


if __name__=="__main__":
    N = int(input())
    # bound를 N으로만 하면 되는거 아님?
    r1,c1,r2,c2 = map(int, input().split())
    dirs = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]
    vis = [[False]*N for _ in range(N)]
    Q = deque()

    # 0,0에서 시작한다는 조건문 - start,end 굳이 명시할 이유가 없음
    print(bfs())