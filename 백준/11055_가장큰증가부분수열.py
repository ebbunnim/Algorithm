import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    D = [0]*N
    for i in range(N):
        for j in range(i,-1,-1):
            if N_list[i]>N_list[j] and D[i]<D[j]:
                D[i] = D[j]
        D[i]+=N_list[i]
    print(max(D))