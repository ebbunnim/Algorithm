import sys
sys.stdin = open("input1.txt","r")


l = [[0]*101 for _ in range(101)]

N = int(input()) #색종이 장수, index로 활용해야함
cnt = [0] * (N+1) #아래에서 N+1로 받을거면 0 인덱스는 더미변수가 됨.

# 우선순위가 있도록 색종이 위치시키고 몇번째 색종이인지 명시하기
for i in range(1,N+1):
    idx_r, idx_c, len_r, len_c = map(int,input().split())
    for row in range(idx_r, idx_r+len_r):
        for col in range(idx_c, idx_c+len_c):
            l[row][col] = i

# 영역을 다 표시했다면,
for a in l: #각 행에 들어있는 리스트
    for e in a : #그 리스트 안에 들어있는 요소들에 접근하겠다.
        if e:
            cnt[e] += 1 # 구분했던 종이의 번호가 인덱스로 들어간 어레이에서 그 인덱스에 +1하겠다.
# print(cnt)
for t in cnt[1:]:
    print(t)