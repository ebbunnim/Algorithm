from collections import deque
import math

def eratos():
    cycle = math.ceil(math.sqrt(9999)) # 최대 cycle 수
    for i in range(2,cycle):
        for j in range(2*i,10000,i):
            eratos_D[j] = False # 소수가 아니다


def bfs(start):
    Q.append((start,0)) # 시작수, 큐의 레벨

    while Q :
        tmp, level = Q.popleft()

        # 탈출 조건
        if tmp == end:
            print(level)
            return

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0: # 맨 앞자리수는 0이면 안됨
                    continue
                # 하나만 바꿔야 함
                new = tmp[:i] + str(j) + tmp[i+1:] # 한자리만 바꿔서 만듬
                # 만든 숫자 중복확인 & 소수여부 확인해서 Q에 넣어야 한다.
                if vis[int(new)] == False and eratos_D[int(new)] == True:
                    vis[int(new)] = True
                    Q.append((new, level+1))



if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        start,end = input().split()
        eratos_D = [True]*10000 # 9999
        eratos()
        vis = [False]*10000 # 만들어놓은 수를 이전에 만들었는지 여부
        Q = deque()
        vis[int(start)] = True
        bfs(start)
