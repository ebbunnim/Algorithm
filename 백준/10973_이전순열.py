def asc():
    for i in range(N):
        if N_list[i:] == sorted(N_list[i:]):
            point = i
            return point
    return N-1


if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    flag = 0

    if N_list == sorted(N_list):
        flag = 1

    if flag == 1:
        print(-1)
    else:
        point = asc()
        for j in range(N-1,point-1,-1):
            if N_list[point-1] > N_list[j]:
                N_list[point - 1], N_list[j] = N_list[j], N_list[point - 1]
                ans = N_list[:point] + sorted(N_list[point:], reverse=True)  # 가장 커야 하므로 내림차순으로 배열

                for e in ans:
                    print(e, end=' ')
                break
