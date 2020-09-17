import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [[0]*N for _ in range(N)]

    for k in range(N):
        for a in range(N):
            for b in range(N):
                if arr[a][k]==1 and arr[k][b]==1:
                    arr[a][b]=1
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=' ')
        print()

