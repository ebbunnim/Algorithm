import sys
sys.stdin = open('input.txt','r')

# two pointer - min(e-s)
if __name__ == '__main__':
    N,S = map(int, input().split())
    N_list = list(map(int, input().split()))
    s, e = 0, 0
    sumv = 0
    ans = N
    flag = 0
    while True:
        if sumv >= S: # e==N일때도 조건에 맞다면 s가 계속 움직여야 하므로 이 자리에 위치해야
            sumv -= N_list[s]
            s += 1
        elif e == N:
            break
        else:
            sumv += N_list[e]
            e += 1
        if sumv>=S:
            flag = 1
            ans = min(ans,e-s)
    if flag == 1:
        print(ans)
    else:
        print(0)