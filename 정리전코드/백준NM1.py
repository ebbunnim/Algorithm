import sys
sys.stdin = open("input.txt", "r")

def backtracking():
    global cnt

    if cnt == M:
        for i in range(N):
            if visited[i] == True:
                print(i+1, end=' ')
        print()
        return


    for i in range(N):
        if visited[i] == False: #들리지 않았다면,
            visited[i] = True
            cnt += 1
            backtracking()
            visited[i] = False
            cnt -= 1

N, M = map(int, input().split())
visited=[False]*N; cnt=0;
backtracking()