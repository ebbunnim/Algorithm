# 배열문제에서 행, 열, 대각선 각각의 합 중에서 max 구하기


for t in range(1, 11):
    test_num = int(input()) #이것 자체를 받으라는 뜻

    l=[]
    for num in range(100):
        N = list(input().split())
        l.append(N)
    #print(l)

    #가로줄 모두 더하기
    l_2=[]
    for colum in range(100):
        sum_row = 0
        for row in range(100): #colunm=0부터 생각하자
            sum_row += int(l[colum][row])
        l_2.append(sum_row)

    #세로줄 모두 더하기
    l_3=[]
    for colum in range(100):
        sum_colum = 0
        for row in range(100): #colunm=0부터 생각하자
            sum_colum += int(l[row][colum])
        l_3.append(sum_colum)

    #대각선 라인 두가지 각각
    sum_cross_right = 0
    for colum in range(100):
        sum_cross_right += int(l[colum][colum])

    sum_cross_left = 0
    for colum in range(100):
        sum_cross_left += int(l[colum][99-colum])

    result=[]
    result.extend(l_2)
    result.extend(l_3)
    result.append(sum_cross_right)
    result.append(sum_cross_left)

    print('#%d %d' % (t,max(result)))