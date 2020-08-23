import sys
sys.stdin = open("input1.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    l = [[0]*M for _ in range(N)] #작아야 append하고 크면 append하지 않음.
    real = [[0]*M for _ in range(N)] #얘로 최종적으로 쓰겠다.
    cnt = [0]*(10+1) #10을 쓰는 이유는 종류가 나와야 하므로
    flag_l = [1]*K
    temp = [0]*K
    breakpoint = 0
    #K는 색종이 장수
    for k in range(K):
        temp[k] = list(map(int,input().split()))

    for k in range(K):
        for i in range(temp[k][0], temp[k][2]+1):
            if breakpoint:
                break
            for j in range(temp[k][1], temp[k][3]+1):
                if temp[k][4] < l[i][j]:  # 이미 명도가 높은 애가 있으면
                    flag_l[k] = 0  # 최종적으로 갱신됨
                    breakpoint = 1 #이중for문 탈출
                    break
                else: #처음에는 무조건 여기 걸림.
                    flag_l[k] = 1
                    l[i][j] = temp[k][4]

    for k in range(K):
        if flag_l[k] == 1:
            for i in range(temp[k][0], temp[k][2]+1):
                for j in range(temp[k][1], temp[k][3]+1):
                    real[i][j] = temp[k][4]


    for a in real:
        for b in a:
            cnt[b] += 1
                # print('cnt배열은',cnt)
    print('flag',flag_l)
    print('real',real)
    print('cnt',cnt)
    print('#%d %d' % (tc,max(cnt)))