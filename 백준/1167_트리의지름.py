import sys
sys.stdin = open('input.txt','r')

from collections import defaultdict, deque

if __name__ == '__main__':
    N = int(input())
    graph = defaultdict(list)
    distance = defaultdict(list)
    for _ in range(N):
        start, *info = list(map(int, input().split()))[:-1]
        for i in range(0, len(info), 2):
            graph[start] += [info[i]]
            distance[start] += [info[i + 1]]

    def bfs(ele):
        Q = deque([ele])
        vis[ele[0]]=True
        while Q:
            curr,dist = Q.popleft()
            save_distance[curr]=dist
            for i in range(len(graph[curr])):
                nxt = graph[curr][i]
                if vis[nxt]==False:
                    vis[nxt]=True
                    Q.append((nxt,dist+distance[curr][i]))
        return

    vis = [True]+[False]*N
    save_distance = [0]*(1+N)
    bfs((1,0))

    idx = save_distance.index(max(save_distance))

    save_distance = [0]*(1+N)
    vis = [True]+[False]*N
    bfs((idx,0))

    print(max(save_distance))