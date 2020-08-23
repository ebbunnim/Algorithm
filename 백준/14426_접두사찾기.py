

if __name__ == '__main__':
    N, M = map(int, input().split())
    texts = [input() for _ in range(N)]
    patterns = [input() for _ in range(M)]
    P = [0]*M


    vis = [False]*M # 패턴 중 이미 접두사라고 처리되면, 굳이 얘를 탐색할 필요가 없다. 접두사 처리 안되었을때만 다른 애의 경우에 접두사 되느냐 볼 수 있고
    for i in range(N):
        for j in range(M):
            flag = 0
            if vis[j] == False:
                for z in range(len(patterns[j])):
                    if texts[i][z] == patterns[j][z]:
                        continue
                    else:
                        flag = 1
                        break
                # 끝까지 같으면
                if flag == 0:
                    vis[j] = True
    print(vis.count(True))
