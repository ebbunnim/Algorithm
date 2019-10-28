# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
T = int(input())

for t in range(1, T + 1):
    base = list(map(int, input().split()))  # K, N, M
    station_l = list(map(int, input().split()))  # 충전기 설치된 위치

    K = base[0]
    N = base[1]
    M = base[2]
    station_l += [N]
    station_l.insert(0, 0)
    # print(station_l) #[0, 1, 3, 5, 7, 9]

    l = []
    for i in range(len(station_l) - 1):  # 사이값 출력이므로 번수 한번 덜 돌아야
        result = station_l[i + 1] - station_l[i]
        l.append(result)

    # print(l) #[1, 2, 2, 2, 2, 1]
    sum_v = 0
    count = 1
    for i in l:
        if i > K:
            count = 0  # 왜? 처음 충전소에서 안세므로 그걸 마지막에 더해주는데 0나와야 하므로
            break

        sum_v += i
        if sum_v <= K:
            # print(f'i={i}')
            continue
            count += 1
            sum = 0
            print(count)
    # print(f'#{t} {count}')