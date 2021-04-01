def solution(n):
    # n이 홀수면 -1 / cnt+1
    # n이 짝수면 2로만 계속 나누기
    # 처리된 결과값으로 1이 나올 때까지 반복
    cnt=1
    while n!=1:
        if n%2:
            n-=1
            cnt+=1
        else:
            n//=2
    return cnt