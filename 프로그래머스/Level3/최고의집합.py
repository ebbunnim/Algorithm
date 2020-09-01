

def solution(n, s):
    if n > s:
        return [-1]
    base = s // n
    result = [base] * n
    idx = 0
    for i in range(s - base * n):
        result[idx] += 1
        idx += 1

    return sorted(result)