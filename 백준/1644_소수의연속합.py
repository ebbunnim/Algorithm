import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    eratos_D = [True]*(1+N)
    cycle = int(N**0.5)
    for i in range(2,cycle): # 시작점
        if eratos_D[i] == True: # 시간절약. 소수는 아닌 애의 배수 볼 필요가 없다.
            for j in range(2*i,N+1,i): # 시작점 배수들
                eratos_D[j] = False
    series =  [i for i in range(2,N+1) if eratos_D[i]==True]

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

