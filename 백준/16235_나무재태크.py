import sys
sys.stdin = open('input.txt','r')
from collections import deque
input=sys.stdin.readline

def spring_and_summer():
    for r in range(N):
        for c in range(N):
            l=len(arr[r][c]) # arr[r][c] 원소들은 오름차순으로 유지되어야 하고, arr[r][c][i]를 update하거나 빼는 과정이 기존 배열의 순서를 해치면 안됨 주의 # 우선순위큐 넣으면 TLE (힙 정렬 시간 소요)
            for i in range(l):
                if rich[r][c]>=arr[r][c][i]:
                    rich[r][c]-=arr[r][c][i]
                    arr[r][c][i]+=1
                else:
                    for _ in range(l-i):
                        age=arr[r][c].pop()
                        rich[r][c]+=(age//2)
                    break

def autumn_and_winter():
    for r in range(N):
        for c in range(N):
            for age_of_tree in arr[r][c]:
                if not age_of_tree%5:
                    for i in range(8):
                        nr,nc=r+dr[i],c+dc[i]
                        if 0<=nr<N and 0<=nc<N:
                            arr[nr][nc].appendleft(1)
            rich[r][c]+=A[r][c]


if __name__ == '__main__':
    N,M,K=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(N)]
    arr=[[deque() for _ in range(N)] for _ in range(N)]
    rich=[[5]*N for _ in range(N)]
    dr=[-1,-1,-1,0,0,1,1,1]
    dc=[-1,0,1,-1,1,-1,0,1]
    for _ in range(M):
        x,y,old=map(int,input().split())
        arr[x-1][y-1].append(old) # 나이

    for _ in range(K):
        spring_and_summer()
        autumn_and_winter()

    cnt=0
    for r in range(N):
        for c in range(N):
            cnt+=len(arr[r][c])
    print(cnt)