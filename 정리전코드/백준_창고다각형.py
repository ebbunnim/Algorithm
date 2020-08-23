import sys
sys.stdin = open("input1.txt", "r")

#어느 방향으로 시작할 것인지를 구분하고, 세부적으로 구분해야
#순서대로 임의값이 설정되지 않으므로 column이 위치되어 있는 범위를 구해야 (양방향, 좌, 우) 판별위해
N = int(input())
col_range = [1001,0] #1000개까지 들어올 수 있다.
col_info = [0]*1001
max_v = 0; max_idx = 0

for _ in range(N):
    x, y = map(int, input().split())
    #col_range에서 x의 범위를 판별한다. (왼쪽 끝, 오른쪽 끝)
    if x < col_range[0]:
        col_range[0] = x
    if x > col_range[1]: #이게 elif이면 안됐음....
        col_range[1] = x
    #가장 큰 기둥을 선택한다.
    if y > max_v:
        max_v = y
        max_idx = x
    #col_index에는 각 시작점(idx)의 기둥의 높이를 적는다.
    col_info[x] = y

max_col=0; result=0;
#탐색할 범위수가 양방향, 좌, 우로 제한을 걸어야

#우측부터 시작
if max_idx == col_range[0]:
    for e in range(col_range[1], col_range[0]-1,-1):
        if col_info[e] > max_col:
            max_col = col_info[e]
        result += max_col

#좌측부터 시작
elif max_idx == col_range[1]:
    for e in range(col_range[0],col_range[1]+1):
        if col_info[e] > max_col:
            max_col = col_info[e]
        result += max_col

#양방향에서 시작

else:
    for e in range(col_range[0], max_idx+1):
        if col_info[e] > max_col:
            max_col  = col_info[e]
        result += max_col

    max_col = 0
    for e in range(col_range[1],max_idx,-1): #여러개 max값이 있어도 커버하려면?
        if col_info[e] > max_col:
            max_col  = col_info[e]
        result += max_col

print(result)




