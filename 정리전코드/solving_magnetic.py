import sys
sys.stdin = open("input.txt","r")

#아래로만 쭉 내림. 이유는? 어차피 갱신된 자료에서 계속 반복될 패턴이므로
#index out of range 막기 위해서
def iswall(arr,i,j):
    if i < 0:
        arr[i+1][j] = 0
        return True
    if i >= N:
        arr[i-1][j] = 0
        return True
    return False

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int,input().split()))
    cnt=0;
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                if not iswall(arr, i + 1, j):
                    if arr[i+1][j] == 0: #index out of range?
                        arr[i][j] = 0
                        arr[i+1][j] = 1
                    elif arr[i+1][j] == 2:
                        cnt+=1 #1)out of range할때도 +1
            elif arr[i][j] == 2:
                if not iswall(arr, i - 1, j):
                    if arr[i-1][j] == 0:
                        arr[i][j] = 0
                        arr[i-1][j] = 2
                    elif arr[i-1][j] == 1:
                        cnt+=1

    print('#%d %d' % (tc, cnt//2))