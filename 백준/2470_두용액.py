import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()
    s, e = 0, N-1
    sumv = N_list[s]+N_list[e]
    start, end = N_list[s], N_list[e]
    ans = 2000000000
    while s<e: # 인덱스 에러가 날 수가 없다. 이렇게 설정하면
        if abs(sumv) <= ans:
            ans = abs(sumv)
            start, end = N_list[s], N_list[e]
            if abs(sumv)==0:
                break
        # 투 포인터
        if sumv > 0:
            sumv -= N_list[e]
            e -= 1
            sumv += N_list[e]
        elif sumv<0:
            sumv -= N_list[s]
            s += 1
            sumv += N_list[s]

    res = [start, end]
    res.sort()
    for r in res:
        print(r, end=' ')

