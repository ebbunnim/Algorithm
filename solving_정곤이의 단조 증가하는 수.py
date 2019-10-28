import sys
sys.stdin = open("input.txt","r")

#단조증가가 멈추는
def monoincrease(n):
    flag = 0
    max_v = 0
    for t in n:
        if int(t) >= max_v:
            max_v = int(t)
            continue
        if int(t) < max_v:
            temp = n
            flag = 1
            break #이 경우에만 감소함.

    if flag == 1:
        return False
    else:
        return True #모든게 다 단조증가합니다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(str, input().split()))
    # print(numbers)

    temp_l = []
    for number in numbers:
        if monoincrease(number): #True인 애들에 대해서만
            temp_l.append(number)
    # print(temp_l)
    if len(temp_l) == 0: #단조증가하는애들이 없다면,
        final = -1

    mymax = 0
    for i in range(len(temp_l)-1):
        for j in range(i+1, len(temp_l)):
            if int(temp_l[i]) * int(temp_l[j]) > mymax:
                mymax = int(temp_l[i]) * int(temp_l[j])
                final = mymax
    print('#%d %d' % (tc, final))