import sys
sys.stdin = open("input.txt", "r")


def connected(x, y): #튜플을 처리하는 isfit함수
    if x[0] == y[0]: return True
    if x[0] == y[1]: return True
    if x[1] == y[0]: return True
    if x[1] == y[1]: return True
    return False
# 하나의 노드라도 연결되면 fit한 것이다.

def BFS(S, G): #start, goal을 만나면 끝나는 함수를 정의
    flag = 0 #1이 되면 while문을 탈출한다.
    #시작 큐 설정
    for k in l:
        if k[0] == S or k[1] == S: #둘 중 하나라도 S에서 시작할 수 있다면,
            Q.append(k)
            visited.append(k) #visited에 넣는 이유는 중복을 없애기 위해서?


    #큐의 역할은 pop과 append로 간선의 역할을 하는 것이다.
    cnt = 0
    while Q: #Q가 계속 pop 되어서 없어질때까지 계속함
        a = Q.pop(0) #독립적으로 리스트 만들려면 여기서 pop해야?
        #여기서 pop하면
        if flag == 1:
            break
        for g in l: #하나라도 연결되면 됨. g, Q의[0][1] or Q[0][0]이면 됨
            if connected(a,g) and g not in visited: #연결되어 있다면, 계속 맨앞의 value에 대해서만 조정
                #골을 찾으면 break조건을 건다.
                if g[0] == G or g[1] == G: #하나라도 G와 연결되어 있다면, 간선에 추가하고 탈출
                    flag = 1
                    cnt += 1
                    break

                # G를 찾지 못한 상태라면,
                Q.append(g) #튜플 형태로 그대로 더한다.
                visited.append(g)
                cnt += 1
            #여기까지 연관된 간선들이 나와야
    return cnt




if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        V, E = map(int, input().split())
        # print(V, E)
        l = [0]*E
        for i in range(E):
            a, b = map(int, input().split())
            l[i] = (a, b)
        # print(l)
        S, G = map(int, input().split())
        # print(S, G)

        # 시작점에서 어떻게 Goal까지 갈 것인가에 대한 문제
        # 노드 거리는 어떻게 취급할 것인가?


        Q = []
        visited = []

        # visited는 연결된 노드에 대해서 지나왔음을 체크하는 리스트
        # Q의 역할은 연결된 애들을 BFS로 독립적으로 체크한 후에 만약에 S에서 G로 이어지면 break, cnt
        result = BFS(S, G)
        # print(result+1)
        print('#%d %d' % (tc,result+1))