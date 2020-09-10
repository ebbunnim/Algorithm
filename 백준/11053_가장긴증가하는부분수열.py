import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    D = [0]*N
    D[0] = 1
    for i in range(1,N):
        maxv = 0
        for j in range(i,-1,-1):
            if N_list[j] < N_list[i]:
                if D[j] > maxv:
                    maxv = D[j]
        D[i] = maxv+1
    print(max(D))