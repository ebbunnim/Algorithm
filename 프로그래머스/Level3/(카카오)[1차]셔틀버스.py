def solution(n, t, m, timetable):
    def maketime(x):
        hour, minute = divmod(x, 60)
        hour = str(hour)
        minute = str(minute)
        if len(hour) == 1:
            hour = '0' + hour
        if len(minute) == 1:
            minute = '0' + minute
        return hour + ':' + minute

    def remain_rows(terminal_time):
        T = []
        for p in timetable:
            hour, minute = map(int, p.split(":"))
            total = 60 * hour + minute
            if total <= terminal_time:  # 1차로 정제
                T.append(total)
        T.sort()
        return T

    terminal_time = 9 * 60 + (n - 1) * t  # 이때까지 타야함. 9시부터 카운트
    T = remain_rows(terminal_time)
    end = 540  # 9시
    for i in range(1, n + 1):
        if i == n:  # 마지막 순회
            # m명보다 작아야 내가 탈 수 있어.
            if len(T) < m:  # 탈 수 있다.
                return maketime(end)
            else:
                # 그게 아니라면 마지막 시간대를 찾아야
                for _i in range(m):
                    if _i == m - 1:
                        return maketime(T[0] - 1)  # 걔보단 1초 앞서서 타야한다.
                    if T[0] <= end:
                        T.pop(0)
                    else:
                        return maketime(end)
        for _ in range(m):  # 돌려
            if T and T[0] <= end:
                T.pop(0)
        end += t  # 다음 번 end 시간