import sys

sys.stdin = open("input1.txt", "r")


N = int(input());
flag = 1
l = [0] * N
for i in range(N):
    l[i] = list(map(int, input().split()))
print(l)
result_l = []

# start, end point를 잡는다.
for i in range(N):
    if flag == 0:
        break
    for j in range(N):
        if flag == 0:
            break

        if l[i][j] != 0:
            start_i = i;
            start_j = j
            end_i = start_i;
            end_j = start_j
            # 열 기준으로 순회하며 0을 만나기 직전의 열의 인덱스를 뽑아놓는다.
            while True:
                end_j += 1;
                if l[end_i][end_j] == 0:
                    end_j -= 1
                    flag = 0  # 해당 열을 탈출시켜줄 flag
                    break
    flag = 1
    while True:
        end_i += 1;
        if l[end_i][end_j] == 0:
            end_i -= 1
            flag = 0
            break  # 행 기준 for문을 탈출한다.
result_l.append((end_i - start_i+1, end_j - start_j+1))  # 행, 열 기준
print(result_l)
for i in range(start_i, end_i + 1):
    for j in range(start_j, end_j + 1):
        l[i][j] = 0
print(l)
print('start&end', start_i, end_i, start_j, end_j)




