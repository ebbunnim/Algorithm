import sys
sys.stdin = open("input.txt", "r")

if __name__=="__main__":
    for tc in range(1, int(input())+1):
        N, M = map(int, input().split())
        path = [[0]*(N+1) for _ in range(N+1)]
        for _ in range(M):
            a, b = map(int, input().split())
            path[a][b]=1
            path[b][a]=1
        ans = 0
        for i in range(1, N+1):
            if path[1][i]:
                ans += 1
        if ans == 0:
            print('#%d %d' % (tc, 0))
            continue
        visited = [0]*(N+1)
        for i in range(2, N + 1):
            if path[1][i]:
                for j in range(2, N + 1):
                    if path[i][j] and not path[1][j] and not visited[j]:
                        visited[j] = 1
                        ans += 1
        print('#%d %d' % (tc, ans))

