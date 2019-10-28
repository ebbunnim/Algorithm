import sys
import copy
sys.stdin = open('input.txt','r')


def backtracking(): #x 는 결국 num만큼 진행되어야 한다.0부터 시작해야
    global mycnt, value, result

    if mycnt == num:
        print('여기')
        if value not in result:
            result.append(value)
        value = value_2
        return


    for i in range(N-1):
        for j in range(i,N):
            if i < j and (i, j) not in visited:
                print(11111)
                value[i], value[j] = value[j], value[i]
                visited.append((i,j)) #이건 재귀 돌때 같은 인덱스로 똑같이 돌지 말라는 제어
                mycnt += 1
                backtracking()
                visited.remove((i,j))
                value[j], value[i] = value[i], value[j]
                mycnt -= 1


if __name__=="__main__":
    temp, num = input().split()
    value = [int(x) for x in temp]
    N = len(value)
    num = int(num)
    print(value)
    # mycnt는 num에 따라 가는애, cnt는
    mycnt=0; result=[]
    value_2 = copy.deepcopy(value) # value_2는 다시 value를 갱신해주는
    visited=[]
    backtracking()
    print(result)