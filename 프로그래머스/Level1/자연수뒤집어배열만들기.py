def solution(n):
    n=str(n)
    m=len(n)
    answer = [0]*m
    for i in range(m-1,-1,-1):
        answer[m-1-i]=int(n[i])
    return answer