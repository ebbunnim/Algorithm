import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = list(map(int,input().split()))
    # 자연수, 연이은 합 : 투 포인터 알고리즘
    s, e = 0, 0
    sumv, ans = 0, 0
    idx = 0
    while True:
        idx += 1
        if sumv >= M:
            sumv -= N_list[s]
            s += 1
        else:
            if e == N: # e가 이미 끝까지 돈 상태다.
                break
            sumv += N_list[e]
            e += 1
        if sumv == M:
            ans += 1
    print(ans)




