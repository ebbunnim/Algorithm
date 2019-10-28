import sys
sys.stdin = open("input.txt", "r")


def mysort(l): #[(3, 4), (4, 5), (2, 3)] 이런꼴로 나와야
    temp = 0;
    temp_info = [0] * (len(l));
    for i in range(len(l)):
        temp = l[i][0] * l[i][1]
        temp_info[i] = (i, temp)
    print(temp_info)
    max_v = 0; mylist = [0]*len(temp_info)
    for k in temp_info:
        if k[1] >= max_v:
            max_v = k[1]
    for i in range(len(temp_info)):
        mylist[i] = max_v
        mysort(l)



N = int(input()); flag=1; flag2=1;
l = [0]*N
for i in range(N):
    l[i] = list(map(int, input().split()))
result_l = [];
i=0; j=0

while True:
    for i in range(N):
        if flag2 == 0:
            break
        for j in range(N):
            if flag == 0 :
                break
            if l[i][j] != 0:
                start_i = i; start_j = j
                end_i = start_i; end_j = start_j
                #열 기준으로 순회하며 0을 만나기 직전의 열의 인덱스를 뽑아놓는다.
                while True:
                    end_j += 1;
                    if l[end_i][end_j] == 0:
                        end_j -= 1
                        flag = 0 #해당 열을 탈출시켜줄 flag
                        break
                    else:
                        if end_j == N-1:
                            end_j = N-1
                            flag = 0
                            break

                while True:
                    end_i += 1;
                    if l[end_i][end_j] == 0:
                        end_i -= 1
                        flag2 = 0
                        break #행 기준 for문을 탈출한다.
                    else:
                        if end_i == N-1:
                            end_i = N-1
                            flag = 0
                            break


    # print('start&end',start_i, end_i, start_j, end_j)
    result_l.append((end_i-start_i+1,end_j-start_j+1)) #행, 열 기준
    for i in range(start_i, end_i+1):
        for j in range(start_j, end_j+1):
            l[i][j] = 0

    #최종 탈출조건
    temp=0
    for i in range(N):
        for j in range(N):
            temp += l[i][j]
    if temp == 0:
        break #가장 상위for문 탈출

    #일단 초기화 하고 시작
    start_i = 0; start_j = 0; end_i = 0; end_j = 0;
    flag=1; flag2=1;

print(result_l)
# 출력부분은 남겨둠

for k in temp_info:
#
# final_l=''; min_v = 0
# while temp_info
# for i in range(len(result_l)):
#     if temp_info[i][1] < min_v:
#         min_v = temp_info[i][1]
#         min_idx = i
# final_l += result_l[temp_info.pop(min_idx)[0]]
# print(temp_info)
#






