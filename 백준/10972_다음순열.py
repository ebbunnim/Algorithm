
if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    point = -1
    flag = 0
    for i in range(N-1):
        if N_list[i] < N_list[i+1]:
            flag = 1
            break
    if flag == 0: # 가장 마지막 수열이라 다음 순열이 없다.
        print(-1)
    else: # 다음순열이 있다.
        for i in range(N):
            if N_list[i:] == sorted(N_list[i:],reverse=True):
                point = i  # 감소수열이 시작되는 인덱스
                break
        if point == -1: # 마지막까지 증가수열이었다.
            point = N-1 # 그러면 감소수열은 가장 끝에 요소 하나만을 할당한다.
        # swap
        for i in range(N-1,point-1,-1):
            if N_list[i] > N_list[point-1]:
                N_list[i], N_list[point-1] = N_list[point-1], N_list[i]
                break
        dec = sorted(N_list[point:N]) # 감소수열이었던 애 오름차순 정렬
        for e in (N_list[0:point] + dec):
            print(str(e), end=' ')
