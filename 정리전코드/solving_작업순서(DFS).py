import sys
sys.stdin = open("input.txt","r")

T = 10
for tc in range(1, T+1):

    def dfs(v): #v는 첫번째 start value, 예를 들면 4 또는 8
        stack=[]; path=''
        stack.append(v)

        while stack: #stack이 존재한다면 - 즉, 탐색할 곳이 남아있다면
            for i in range(len(stack)) :
                pop_v = stack.pop()
                if visited[pop_v] > 0:
                    visited[pop_v] -= 1
                if visited[pop_v] == 0:
                    visited[pop_v] = 'FIN'
                    path += str(pop_v)
                    path += ' '
                    stack.extend(adj_l[pop_v])
        return path

    if __name__=="__main__":
        V, E = map(int, input().split()) # E는 간선, V는 정점 범위
        l = list(map(int, input().split()))
        start = [l[i] for i in range(E * 2) if not i % 2]
        end = [l[i] for i in range(E * 2) if i % 2]

        # 인접리스트를 만든다. : [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
        adj_l = [[] for i in range(V+1)];
        for idx in range(0, V+1):
            for j in start:
                if idx == j:
                    temp = start.index(j)
                    start[temp] = 0
                    adj_l[idx].extend([end[temp]])
        # visited리스트를 만든다. [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]
        visited = [0 for i in range(V + 1)];
        for idx in range(0, V+1):
            visited[idx] = end.count(idx)

        #결과값 산출
        dfs_v=''
        for i in range(1, V+1):
            if visited[i] == 0:
                dfs_v += dfs(i)
        print('#%d %s' % (tc, dfs_v))
        print(len(dfs_v))
        print(len(sorted(dfs_v)))

