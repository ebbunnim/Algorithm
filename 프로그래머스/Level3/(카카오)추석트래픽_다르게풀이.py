from datetime import datetime, timedelta

def solution(lines):
    def check(t):
        cnt = 0
        for i in range(len(S)):
            if E[i] >= t and S[i] <= t + timedelta(seconds=0.999):
                cnt += 1
        return cnt

    S, E = [], []
    for line in lines:
        line = line.split(' ')
        end = datetime.strptime(line[0] + ' ' + line[1], '%Y-%m-%d %H:%M:%S.%f')
        delta = timedelta(seconds=float(line[2][:-1]))
        start = end - delta + timedelta(seconds=0.001)
        S.append(start)
        E.append(end)

    _max = 0
    for i in range(len(S)):
        _max = max(_max, check(S[i]), check(E[i]))
    return _max