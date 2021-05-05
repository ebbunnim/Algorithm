import sys
from copy import deepcopy
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def mat_mul(arr1,arr2):
    res=[[0]*N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                res[i][j]+=arr1[i][k]*arr2[k][j]
    for i in range(N):
        for j in range(N):
            res[i][j]%=1000
    return res

def divide_and_conquer(bin_num:str):
    ans = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
    for idx,val in enumerate(bin_num[::-1]):
        if val=='1':
            tmp=deepcopy(arr)
            for _ in range(idx):
                tmp=mat_mul(tmp,tmp)
            ans=mat_mul(tmp,ans)
    return ans

if __name__ == '__main__':
    N,B=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    bin_B=bin(B)[2:]
    ans=divide_and_conquer(bin_B)
    for row in ans:
        print(*row)

