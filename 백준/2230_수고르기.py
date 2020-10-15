import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N, M = map(int,input().split())
    Nlist = [int(input()) for _ in range(N)]
    s, e = 0, 1
    # e : M보다 작으면 포인터를 키움. s는 M보다 크면 키움. s<e 이도록 포인터 조정
    diff = 0
    minv = 4000000001
    Nlist.sort()
    while True:
        diff = abs(Nlist[s]-Nlist[e])
        if diff >= M:
            minv = min(minv, diff)
        if diff < M and e != N-1:
            e += 1
        else:
            s += 1
            if s == e:
                if e != N-1:
                    e += 1
        if s == N-1:
            break

    print(minv)
