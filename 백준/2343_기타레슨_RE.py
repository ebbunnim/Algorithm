import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N, M = map(int,input().split())
    Nlist = list(map(int, input().split()))

    # lower bound (같은 값 - 가장 온쪽)
    # M개를 고르겠다. 근데 가능한 최소로
    def binary_search():
        s, e = max(Nlist), sum(Nlist) # 값 자체를 찾겠다. + s 주의 (트랙의 길이 반으로 쪼개면 안됨 )
        while s<e:
            mid = (s+e)//2

            group = 1
            sumv = 0
            for i in range(N):
                sumv += Nlist[i]
                if sumv > mid:
                    group += 1
                    sumv = Nlist[i]

            if group > M : # 더 많이 쪼개졌다면
                s = mid + 1
            else:
                e = mid

        return e
    print(binary_search())

