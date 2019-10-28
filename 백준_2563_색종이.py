import sys
sys.stdin = open("input1.txt","r")

arr = [[0]*100 for _ in range(100)]

K = int(input()) #색종이수
for k in range(K):
    #좌측, 하단으로 받음, 무조건 길이는 10씩임. 겹치는 부분
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
cnt=0
for a in arr:
    for b in a:
        if b == 1:
            cnt+=1
print(cnt)
