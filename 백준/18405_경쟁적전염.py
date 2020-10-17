import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    N, K = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())

    virus = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=0:
                virus.append((arr[i][j],i,j,0)) # 바이러스종류,행,열,시간
    Q = deque(sorted(virus)) # sort 작업을 해야 바이러스 번호 낮은 것을 우선으로 퍼지기 시작함. 나중에 큐에 들어오는 애들도 다 오름차순

    def spread(v,r,c,t):
        for dr, dc in (-1,0),(1,0),(0,-1),(0,1):
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
                arr[nr][nc]=v # 바이러스 번호
                Q.append((v,nr,nc,t+1))

    while Q:
        curr_virus = Q.popleft()
        if curr_virus[3]==S: # pruning
            break
        spread(curr_virus[0],curr_virus[1],curr_virus[2],curr_virus[3])


    print(arr[X-1][Y-1])

    # 0이 없는 상황일 때 순회 멈춰야 하고, 우선 순위에 따라서 순회가 이어져야 한다. 최단거리보단 FIFO 구조에 더 초점 맞춰진 문제

    #<요구사항>
    # 번호가 낮은 애부터 순서대로 증식된다. 먼저 채워진 칸은 바꿀 수 없다.
    # 처음에 arr에 있는애들 바이러스 번호를 list에 옮긴다.
    # 각 리스트 원소들씩 계속 순회하면서 바이러스를 상하좌우로 증식한다.
    # 이때, 0이 아니라면, 침범하지 못하는 것과 함께 list를 오름차순으로 순회해서 바이러스의 우선순위 매기는 것 주의
    # deepcopy 필요없어. back 할게 없으니까.