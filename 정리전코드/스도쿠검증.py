import sys
sys.stdin = open("input1.txt", "r")


def fit(l):
    cnt = 0
    for e in [1,2,3,4,5,6,7,8,9]:
        if e in l:
            cnt += 1
    if cnt == 9 and len(l) == 9: #1~9요소가 다 들어있고 정확히 9개만 존재한다면,
        return True
    return False


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        l = [0]*9
        for i in range(9):
            l[i] = list(map(int,input().split()))

        cnt_1=0; cnt_2=0; cnt_3=0;
        result_1=0; result_2=0; result_3=0; #default값 정의
        #가로검증
        for i in range(9):
            if fit(l[i]):
                cnt_1 += 1
        if cnt_1 == 9:
            result_1 = 1
        #세로검증 (행 우선순회)
        temp = []
        for j in range(9):
            temp=[]
            for i in range(9):
                temp += [l[i][j]]
            if fit(temp):
                cnt_2 += 1
        if cnt_2 == 9:
            result_2 = 1
        #영역별 검증
        temp=[]
        for i in range(3):
            for j in range(3):
                row = 3 * i
                col = 3 * j
                for a in range(3):
                    for b in range(3):
                        temp += [l[row + a][col + b]]
                if fit(temp):
                    cnt_3 += 1
                temp = []
        if cnt_3 == 9:
            result_3 = 1

        #마지막 결과를 산출한다.
        if result_1 and result_2 and result_3:
            print('#%d %d' % (tc,1))
        else:
            print('#%d %d' % (tc,0))