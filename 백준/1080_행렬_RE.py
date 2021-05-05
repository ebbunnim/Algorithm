import sys
sys.stdin = open('input.txt','r')

def switch(arr,r,c):
    for i in range(3):
        for j in range(3):
            arr[r+i][c+j]=not arr[r+i][c+j]


if __name__ == '__main__':
    N,M=map(int,input().split())
    A=[list(map(int,input())) for _ in range(N)]
    B=[list(map(int,input())) for _ in range(N)]
    height=N-2
    width=M-2
    ans=0
    for i in range(height):
        for j in range(width):
            if A[i][j]!=B[i][j]:
                switch(A,i,j)
                ans+=1
    flag=0
    for i in range(N):
        for j in range(M):
            if A[i][j]!=B[i][j]:
                flag=1
                break
        if flag:
            break
    if flag:
        print(-1)
    else:
        print(ans)




