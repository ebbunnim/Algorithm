
def dfs(i, j):
    global cnt, max_val

    max_val = max(max_val, cnt)

    for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni = i + a
        nj = j + b
        if 0<=ni<N and 0<=nj<M:
            if bins[ord(arr[ni][nj])-65] == True:
                continue
            else:
                bins[ord(arr[ni][nj])-65] = True
                cnt += 1
                dfs(ni,nj)
                bins[ord(arr[ni][nj])-65] = False
                cnt -= 1
    #(*)
if __name__ == '__main__':
    N,M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    bins = [False]*26
    cnt = 1
    max_val = 0
    # 무조건 처음에는 0,0 idx 에서 시작해야 한다는 조건때문에 고정함
    bins[ord(arr[0][0])-65] =  True
    dfs(0,0)
    print(max_val)
