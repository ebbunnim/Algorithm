import heapq
from collections import deque

def find_delay_works(jobs, waiting, t):
    # 현재 t에서 대기해야 되는 작업 있는지 확인
    while jobs and jobs[0][0] <= t:
        waiting_job = jobs.popleft()
        heapq.heappush(waiting, (waiting_job[1], waiting_job[0]))  # 소요시간 우선순위


def solution(jobs):
    N = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    sumv = 0

    waiting = []

    while jobs:
        # 대기 중인 작업이 없을 때
        job = jobs.popleft()
        t = job[0] + job[1]  # job[0]은 0 이 아닐 수 있음 주의!!!!!!!!!
        sumv += job[1]  # 소요시간

        # 현재 t에서 대기해야 되는 작업 있는지 확인
        find_delay_works(jobs, waiting, t)

        # 현재 대기중인 애들에 관해서, 걸린 시간들을 더하면 된다.
        while waiting:
            waited_job = heapq.heappop(waiting)  # 한 작업만을 뺀다. 소요시간 짧은 애
            sumv += (t - waited_job[1]) + waited_job[0]  # 기다린 시간 + 소요시간
            t += waited_job[0]
            find_delay_works(jobs, waiting, t)

    return sumv // N


# 반례 - 이게 8 나와서 고생했었음 ㅠ.ㅠ
# [[1, 10], [3, 3], [10, 3]], 9