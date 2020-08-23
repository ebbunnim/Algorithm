if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key=lambda x : (x[1], x[0]))


    end = arr[0][1]
    cnt=1
    for i in range(1,N):
        if end <= arr[i][0]:
            cnt += 1
            end = arr[i][1]
    print(cnt)
