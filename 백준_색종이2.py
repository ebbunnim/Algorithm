import sys
sys.stdin = open("input1.txt","r")

# 색종이들 위치에 대해서 나중에 위치한 종이에 대해서 우선순위가 있음.
# 각 색종이가 가지고 있는 면적을 구해야
# 인덱스는 각 면적의 왼쪽아래  시작점을 가리킨다. (겹치는 부분에 대한 제어필요)


N = int(input())
paper = [[0]*101 for _ in range(101)]
cnt = [0]*(N+1)
for n in range(1, N+1):
    data = list(map(int, input().split()))
    for i in range(data[0], data[0]+data[2]):
        for j in range(data[1], data[1]+data[3]):
            paper[i][j] = n
print('paper',paper)
# 색종이의 갯수, 평면의 크기가 작아서 (<= 100) 색종이가 들어올 때 마다 색종이가 덮는 구역의 값을 그 색종이의 index로 설정해주기만 하면 됩니다. 초등부 문제답게 복잡한 알고리즘이 필요 없고 구현만 실수 없이 하면 됩니다.
for e in paper:
    print('e',e)
    for a in e:
        print('a',a)
        if a :
            cnt[a] += 1
print(cnt)
for e in cnt[1:]:
    print(e)

