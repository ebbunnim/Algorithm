# 칠해야 할 사각형 영역 내에 새로 칠할 명도보다 더 높은 명도 번호를 가지는 영역이 존재한다면,
# 해당 사각형 영역에 대해서는 색을 칠하지 않아야 한다.
# 가장 큰 영역을 출력해야
import sys
sys.stdin = open("input1.txt","r")

T = int(input())
for tc in range(1, T+1):

    N, M, K = map(int,input().split())
    #항상 행과 열이 주어지면 '도화지' 역할을 한다. 기준 arr를 만들어야
    l = [[-1]*M for _ in range(N)]
    #종류별로 인덱스를 기준으로 받고 cnt할 cnt를 만든다.
    cnt = [0]*(10+1) #K는 색종이 종류이므로 여기서는 명도를 기준으로 나누니까 10 기준

    #K는 색종이 장수
    max_v = 0
    for _ in range(K): #K가 의미가 있냐?
        temp = list(map(int,input().split()))
        if temp[4] >= max_v:
            max_v = temp[4] #이 제약을 왜 줬어? ->
        for i in range(temp[0], temp[2]+1): #이거 인덱스 조정해야
            for j in range(temp[1], temp[3]+1):
                #근데 이러면 조금이라도 겹치면 아예 색종이를 올려놓지 못한다는 조건에 부합하지 않음.
                if max_v <= temp[4]: #더 낮은 명도가 오면 아예 값을 명시하지 못한다.
                    l[i][j] = temp[4]

    for a in l:
        for b in a: #배열의 요소 하나하나에 접근하고 싶다.
            if b:
                cnt[b] += 1 #cnt는 배열이다. 여기서 max를 구해야(값이자 인덱스 역할을 하는 수라는 것에 주의)
    print(cnt)
    # print('#%d %d' % (tc, result))
    print(max(cnt))

'''
5
5 5 1
1 0 4 3 3
5 5 4
0 2 2 3 5
1 2 2 3 5
1 0 4 2 5
2 3 4 4 3
7 7 3
5 1 6 5 0
5 4 5 5 0
2 0 5 6 2
7 7 5
4 2 6 2 2
5 0 5 5 3
0 0 6 3 0
0 4 3 6 2
5 1 5 4 0
10 10 5
2 7 9 9 2
6 1 9 3 7
4 0 9 9 2
8 8 9 8 2
4 5 6 8 10


'''
# 칠해야 할 사각형 영역 내에 새로 칠할 명도보다 더 높은 명도 번호를 가지는 영역이 존재한다면,
# 해당 사각형 영역에 대해서는 색을 칠하지 않아야 한다.
# 가장 큰 영역을 출력해야
import sys
sys.stdin = open("input1.txt","r")

N, M, K = map(int,input().split())
#항상 행과 열이 주어지면 '도화지' 역할을 한다. 기준 arr를 만들어야
l = [[-1]*M for _ in range(N)]
#종류별로 인덱스를 기준으로 받고 cnt할 cnt를 만든다.
cnt = [0]*(10+1) #K는 색종이 종류이므로 여기서는 명도를 기준으로 나누니까 10 기준

#K는 색종이 장수
max_v = 0
for _ in range(K): #K가 의미가 있냐?
    temp = list(map(int,input().split()))
    if temp[4] >= max_v:
        max_v = temp[4] #이 제약을 왜 줬어? ->
    for i in range(temp[0], temp[2]): #이거 인덱스 조정안해도 되게 우측하단인거 아님?
        print('1',temp[0], temp[2])
        for j in range(temp[1], temp[3]+1):
            print('2',temp[1], temp[3]+1
            #근데 이러면 조금이라도 겹치면 아예 색종이를 올려놓지 못한다는 조건에 부합하지 않음.
            if max_v <= temp[4]: #더 낮은 명도가 오면 ***그리고 겹치는 부분이 있다면*** 아예 날려야
                l[i][j] = temp[4]

for a in l:
    for b in a: #배열의 요소 하나하나에 접근하고 싶다.
        #-1을 찍으면 여기서 가장 마지막 배열에 카운트하게 되는 오류가 뜸.
        # print('b는 여기입니다.',b)
        if b != -1: #0인 종류도 count해야 했으므로 여기서 -1이 아닌 수를 배열에 넣겠다는 선언해야
            cnt[b] += 1 #cnt는 배열이다. 여기서 max를 구해야(값이자 인덱스 역할을 하는 수라는 것에 주의)
            # print('cnt배열은',cnt)
print(cnt)
print(max(cnt))

'''
2 : (2, 7)~(9, 9) 7*2 = 14
7 : (6, 1)~(9, 3) : (x는 6~9 겹침, y는 겹치지 않음. ) = 6
2: (4, 0)~(9, 9)
2 : (8, 8)~(9, 8)
10: (4, 5)~(6, 8)

'''