import sys
sys.stdin = open('input.txt','r')

# 가로로 겹치지 않게 M 만큼의 벌통을 두명이 확보 : 두번째 조합
# 최대총량 C 안에서, 최대이익을 벌 수 있도록 뽑아야(단, 이때 뽑아야 하는 개수가 정해지지 않은상태) : 첫번째 조합
# Start point: M 만큼의 벌통을 채취할 수 있는 모든 시작점에 조건에 맞는 최대수익을 저장해놓자

def honey(arr_M):
    maxv=0
    for i in range(1, (1<<M)):
        res1 = 0; res2 = 0
        for j in range(M):
            if i & (1<<j): #i 의 j번째 인덱스가 0인지 1인지 확인가능
                res1 += arr_M[j]
                res2 += arr_M[j]**2
        if res1 <= C and res2 > maxv:
            maxv = res2
    return maxv

if __name__=="__main__":
    for tc in range(1, int(input())+1):
        N, M, C = map(int, input().split())
        arr=[list(map(int, input().split())) for _ in range(N)]
        DP = [[0]*N for _ in range(N)]

        for i in range(N): #세로
            for j in range(N-M+1):
                DP[i][j] = honey(arr[i][j:j+M])

        DP = sum(DP, [])
        ans=0
        for i in range(N*N):
            for j in range(i+M, N*N):
                ans = max(ans, DP[i] + DP[j])
        print('#%d %d' % (tc, ans))

