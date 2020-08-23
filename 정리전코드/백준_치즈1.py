import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# 주의할 점 두가지
# cnt 세는 위치에 따라 답이 다르게 나온다는 점
# 안쪽 구멍과 바깥 공기를 다른 상태로 표시하기 위해서 -1로 처리하는 과정이 필요했고, 구멍은 -1을 만나는 순간 외부공기가 된다.




# 공기와 만나는 애 2로 상태표시하는 함수
def isedge1(x, y):
   for i in range(4):
       idx = x + D[i][0]
       idy = y + D[i][1]
       if 0<=idx<N and 0<=idy<M and arr[idx][idy] == -1:
           arr[x][y] = 2

# 0을 모두 -1로 만드는 애
def bfs(x, y): #0,0으로 start이면
   Q.append((x, y))
   vis[x][y] = True
   arr[x][y]=-1
   while Q:
       a = Q.popleft() #좌표 하나를 빼면
       for i in range(4):
           idx = a[0] + D[i][0]
           idy = a[1] + D[i][1]
           if 0<=idx<N and 0<=idy<M and vis[idx][idy]==False and arr[idx][idy]==0:
               arr[idx][idy]=-1
               vis[idx][idy] = True
               Q.append((idx, idy))

if __name__=="__main__":
   N, M = map(int, input().split())
   arr = [list(map(int, input().split())) for _ in range(N)]
   Q = deque(); ans=0; ans2=0
   D = [(0,1), (1,0), (0,-1), (-1,0)]
   vis = [[False]*M for _ in range(N)]
   # 외부공기를 bfs로 돌며 모두 -1로 바꾼다.
   bfs(0, 0)

   # print(*arr, sep='\n')
   while arr != [[-1]*M for _ in range(N)]:
       ans2 += 1
       cnt=0

       for i in range(N):
           for j in range(M):
               if arr[i][j] == 1:
                   isedge1(i, j)
                   cnt += 1

       # 여기서 카운트를 하면 가장자리를 제외하고 세는 격이 됨.
       # cnt=0
       for i in range(N):
           for j in range(M):
               if arr[i][j] == 2:
                   arr[i][j] = -1
               # if arr[i][j] == 1:
               #     cnt += 1
       # print(*arr, sep='\n')

       if cnt != 0:
           ans = cnt

       for i in range(N):
           for j in range(M):
               if arr[i][j] == 0:
                   for a in range(4):
                       idx = i + D[a][0]
                       idy = j + D[a][1]
                       if arr[idx][idy] == -1:
                           bfs(i, j)
                           break
   print(ans2)
   print(ans)

