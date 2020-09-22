import sys
sys.stdin = open('input.txt','r')

from collections import deque

# union-find럼 인거같은데, 굳이 비용 정보 필요 없고, 부모 노드 필요없으니까 bfs로 돌림
# 만약, union-find써버리면 계속 부모노드로 타고 들어가야 함. 아래처
# https://blog.naver.com/sjy263942/222092122588
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        N_list = [0]+list(map(int, input().split()))
        vis = [True]+[False]*N
        def bfs(start):
            Q = deque([start])
            vis[start] = True
            while Q:
                curr = Q.popleft()
                nxt = N_list[curr]
                if vis[nxt] == False:
                    vis[nxt]=True
                    Q.append(nxt)
        cnt = 0
        for i in range(1,N+1):
            if vis[i] == False:
                bfs(i)
                cnt += 1
        print(cnt)

