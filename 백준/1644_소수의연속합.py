import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    # 41 이하의 소수들 리스트 뽑아.
    # 소수인지 확인해서 카운트에 1 더해
    # 나머지는 투 포인터 알고로 풀기

    def eratos():
        eratos_D = [True]*(1+N)
        cycle = int(N**0.5)
        for i in range(2,cycle): # 시작점
            for j in range(2*i,N+1,i): # 시작점의 배수들
                eratos_D[j] = False
        return [i for i in range(2,N+1) if eratos_D[i]==True]
    series = eratos()

    # 투포인터
    s, e = 0, 0
    sumv = 0
    ans = 0
    while True:
        if sumv >= N :
            sumv -= series[s]
            s += 1
        elif e == len(series):
            break
        else:
            sumv += series[e]
            e += 1
        if sumv == N:
            ans += 1
    print(ans)

