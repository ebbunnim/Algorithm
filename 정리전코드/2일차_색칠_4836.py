# 사각형 : (2, 2)~(4, 4) & (3, 3)~(7, 7)
# 겹치는 부분 : 가로 = 3, 4 영역, 세로 = 3, 4 영역
# 가로 : 2~4와 3~7이 겹치는 영역  = 3,4   #index = 0, 2
# 세로 : 2~4와 3~7이 겹치는 영역 = 3,4    #index = 1, 3

# 첫번째로는 color이 1인지 2인지 구분하고 다른 애를 기준으로 묶기

T = int(input())

for t in range(1, T + 1):

    N = int(input())
    l_1 = []; l_2 = []

    for num in range(N):
        position_l = []
        position_l = list(map(int, input().split()))

        if position_l[4] == 1:
            l_1.append(position_l)
        else:
            l_2.append(position_l)
    # print(l_1)
    # print(l_2)

    # 가로 기준 겹치는 부분 알기
    final_result = 0; testing=[0]
    for a in range(len(l_1)):
        for b in range(len(l_2)):
            temp_row = []
            for i in range(l_1[a][0], l_1[a][2] + 1):
                temp_row.append(i)

            temp_row_2 = []
            for j in range(l_2[b][0], l_2[b][2] + 1):
                temp_row_2.append(j)

            result_row = []
            for factor in temp_row:
                if factor in temp_row_2:
                    result_row.append(factor)
            # 마지막에는 len(result)해서 세로 케이스와 곱해야

            # 세로 기준 겹치는 부분 알기
            temp_col = []
            for i in range(l_1[a][1], l_1[a][3] + 1):
                temp_col.append(i)

            temp_col_2 = []
            for j in range(l_2[b][1], l_2[b][3] + 1):
                temp_col_2.append(j)

            result_col = []
            for factor in temp_col:
                if factor in temp_col_2:
                    result_col.append(factor)

            temp = []
            for a in result_row:
                for b in result_col:
                    temp.append((a,b))

            temp_2 = [t for t in temp if t not in testing]
            testing = temp_2 #바로 전 list로 갱신해서 다시 testing

            area = len(temp_2)
            final_result += area

    print('#%d %d' % (t, final_result))

