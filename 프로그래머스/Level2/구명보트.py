from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    Q = deque(people)
    cnt = 0
    while Q :
        heavy = Q.popleft()
        if Q and Q[-1] <= (limit-heavy):
            Q.pop()
        cnt += 1
    return cnt