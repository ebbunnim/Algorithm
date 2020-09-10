def binary(target):
    start = 0
    end = len(D)-1
    while start < end:
        mid = (start+end)//2
        if D[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end


if __name__ == '__main__':
    INF = -1000000001
    N = int(input())
    N_list =[INF]+list(map(int, input().split()))
    D = [INF]
    for i in range(1,N+1):
        if D[-1] < N_list[i]:
            D.append(N_list[i])
        else:
            D[binary(N_list[i])] = N_list[i] # 작은 값으로 갱신. 10-30 이었다면 10-20 으로 해야 더 긴 길이 수열을 찾을 수 있다.
    print(len(D)-1)
