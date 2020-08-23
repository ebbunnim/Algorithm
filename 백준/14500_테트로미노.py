# dfs가 4가지 방향으로 갈 수 있다는 것.
def dfs(i,j,cnt,ans):
    global max_v

    if cnt == 3:
        if ans > max_v:
            max_v = ans
       return

    for a,b in [(-1,0),(1,0),(0,1),(0,-1)]:
        if 0<=i+a<N and 0<=j+b<M and vis[i+a][j+b] == False:
            vis[i+a][j+b] = True
            cnt += 1
            ans += arr[i+a][j+b]
            dfs(i+a,j+b,cnt,ans)
            vis[i+a][j+b] = False
            cnt -= 1
            ans -= arr[i+a][j+b]

def T1(i,j): # ㅜ
    global max_v
    ans = 0
    if i < N and i+1<N and j < M and j +1 < M and j+2 < M:
        ans += arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
        if ans > max_v:
            max_v = ans

def T2(i,j): # ㅏ
    global max_v
    ans = 0
    if i < N and i+1<N and i+2 < N and j < M and j+1 < M:
        ans += arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1]
        if ans > max_v:
            max_v = ans

def T3(i,j): # ㅗ
    global max_v
    ans = 0
    if j < M and j+1<M and j+2 < M and j < M and i<N and i-1 >= 0:
        ans += arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+1]
        if ans > max_v:
            max_v = ans

def T4(i,j): # ㅓ
    global max_v
    ans = 0
    if j < M and j+1<M and i<N and i-1 >= 0 and i+1<N:
        ans += arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i+1][j+1]
        if ans > max_v:
            max_v = ans

if __name__ == '__main__':
    max_v = 0
    N, M = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(N) ]
    vis = [ [False]*M for _ in range(N) ]

    for i in range(N):
        for j in range(M):
            vis[i][j] = True
            dfs(i,j,0,arr[i][j]) # 여기에 될 때마다 0으로 초기화햇어야 했기 떄문에 / max_v는 초기화안하고 한 변수로 계속 써야함 / 처음 시작점은 ans의 첫번째로 더해지는 값이므로 이렇게
            vis[i][j] = False

            T1(i,j)
            T2(i,j)
            T3(i,j)
            T4(i,j)

    print(max_v)
