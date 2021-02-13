def solution(play_time, adv_time, logs):
    def to_sec(str_t):
        h, m, s = map(int, str_t.split(':'))
        return 60 * 60 * h + 60 * m + s

    def to_hour(t):
        h, t = divmod(t, 3600)
        m, t = divmod(t, 60)
        s = t
        return str(int(h)).zfill(2) + ':' + str(int(m)).zfill(2) + ':' + str(int(s)).zfill(2)

    if play_time == adv_time:
        return '00:00:00'

    play_time = to_sec(play_time)
    adv_time = to_sec(adv_time)
    DP = [0] * (play_time + 1)
    for log in logs:
        s, e = log.split('-')
        DP[to_sec(s)] += 1
        DP[to_sec(e)] -= 1

    for i in range(1, play_time + 1):
        DP[i] = DP[i] + DP[i - 1]

    for i in range(1, play_time + 1):
        DP[i] = DP[i] + DP[i - 1]

    maxv = DP[adv_time]
    t = 0
    for i in range(adv_time + 1, play_time + 1):
        tmp = DP[i] - DP[i - adv_time]
        if tmp > maxv:
            t = i - adv_time + 1
            maxv = tmp
    return to_hour(t)