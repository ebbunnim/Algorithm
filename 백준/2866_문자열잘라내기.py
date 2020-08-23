
if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 행을 이분탐색함. 밑에가 중복이라면 위를 다시 탐색, 중복 아니라면 아래를 다시 이분 탐색
    start = 0
    end = N-1
    count = N

    while start<=end:
        flag = 0
        mid = (start+end)//2
        tmp = set()
        for j in range(M):
            word = ''
            for i in range(mid,N):
                word += arr[i][j]
            if word not in tmp:
                tmp.add(word)
            else:
                flag = 1
                if count > mid:
                    count = mid
                else:
                    break
        if flag == 1: # 윗 부분 이진탐색 해야
            end = mid - 1
        else:
            start = mid + 1  # 아래 부분 이진탐색 해야
    print(count-1)
