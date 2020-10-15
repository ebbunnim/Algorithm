import sys
sys.stdin = open('input.txt','r')


# versus leetcode 53

# sum이 M이 되도록, 집합 내 개수는 가변적
# 부분된 연속합 -> 정해진 합 target을 만족하는 지 여부.
# N_list 인덱스는 건들이면 안됨 (sort X)

if __name__ == '__main__':
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    s, e = 0, 0
    sumv = 0
    ans = 0
    while True:
        if sumv >= M:
            sumv -= N_list[s]
            s += 1
        elif e == N:
            break
        else:
            sumv+=N_list[e]
            e+=1

        if sumv == M:
            ans += 1
    print(ans)
