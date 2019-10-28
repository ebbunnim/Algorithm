#case1 한해서
import sys
sys.stdin = open("input.txt","r")

T=int(input())
for tc in range(1, T+1):
    def isdfs(S):
        stack=[]; path=''
        stack.append(S) #S는 str이어야 path로 연결가능

        while stack:
            for _ in range(len(stack)):
                pop_v = stack.pop() #stack에 담겨있는 애들만큼 돌아야
                if visited[pop_v] > 0:
                    visited[pop_v] -= 1
                if visited[pop_v] == 0:
                    visited[pop_v] = 'FIN'
                    path += str(pop_v)
                    stack.extend(adj_l[pop_v])
        print(path)
        if str(S) in path and str(G) in path:
            return 1
        return 0

    if __name__ == "__main__":
        V, E = map(int, input().split())
        l_1=[]; l_2=[]; adj_l=[[] for _ in range(V+1)]
        for i in range(E):
            first, second = map(int, input().split())
            l_1.append(first)
            l_2.append(second)
        visited=[0 for _ in range(V+1)]
        for i in l_2:
            visited[i]=l_2.count(i)
        for idx in range(1, V):
            for j in l_1:
                if idx == j:
                    temp = l_1.index(j)
                    l_1[temp] = 0 #왜 찍었어야? 이거 확인하기.....
                    adj_l[idx].extend([l_2[temp]])
        print('인접리스트',adj_l)
        print(visited)
        S, G = map(int, input().split())

        print('#%d %d' % (tc, isdfs(S)))