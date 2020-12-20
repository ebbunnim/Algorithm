from datetime import datetime
from collections import deque


def solution(lines):
    logs = []
    for line in lines:
        end = datetime.strptime(line[:23], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        logs += [(end, -1)]  # 윈도우에서 카운트해줄 flag 처리
        logs += [(end - float(line[24:-1]) + 0.001, 1)]
    logs.sort()

    maxv = 1
    inprogress = cnt = 0
    Q = deque(logs)
    while Q:
        curr = Q.popleft()
        cnt = inprogress
        if curr[1] == 1:
            cnt += 1
        for nxt in Q:
            if nxt[0] - curr[0] > 0.999:
                break
            if nxt[1] == 1:
                cnt += 1
        maxv = max(maxv, cnt)
        inprogress += curr[1]
    return maxv