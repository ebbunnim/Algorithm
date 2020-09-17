import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,S,M = map(int, input().split())
    N_list = list(map(int, input().split()))
    # D[i][v] = i번째에 v를 만들 수 있나?
    D = [[0]*(1+M) for _ in range(N+1)]
    D[0][S] = 1

    for i in range(N):
        for v in range(M+1):
            if D[i][v] == 1:
                if 0<=v+N_list[i]<=M:
                    D[i+1][v+N_list[i]] = 1
                if 0<=v-N_list[i]<=M:
                    D[i+1][v-N_list[i]] = 1

    flag = 0
    for i in range(M,-1,-1):
        if D[N][i] == 1:
            print(i)
            flag = 1
            break
    if flag == 0:
        print(-1)
