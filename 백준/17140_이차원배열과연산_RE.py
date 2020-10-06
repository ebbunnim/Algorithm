import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')

from collections import Counter
from copy import deepcopy

if __name__ == '__main__':
    r,c,k = map(int, input().split())
    r -= 1
    c -= 1
    arr = [list(map(int, input().split())) for _ in range(3)]
    R, C = 3, 3
    t = 0

    def calculate():
        global t, R, C , arr

        while True:
            t += 1
            if t > 100:
                print(-1)
                return

            if R >= C:  # R 연산. 각 행에서 연산. 정렬은 열 원소들
                tmp_arr = []
                for row in arr:
                    counter = Counter(row)
                    sortedlist = sorted(list(counter.items()), key=lambda x: (x[1], x[0]))
                    nrow = []
                    for s in sortedlist:
                        if s[0] == 0:
                            continue
                        nrow += [s[0]]
                        nrow += [s[1]]
                    tmp_arr += [nrow[:100]]
                    C = max(C, len(nrow))
                # full by zero
                for row in tmp_arr:
                    for _ in range(C-len(row)):
                        row += [0]

                arr = deepcopy(tmp_arr)
            else:  # C 연산. 각 열에 대해서 연산. 정렬은 행 원소들 => transpose가 필요하다.
                trans_arr = list(map(list, zip(*arr)))  # transpose
                tmp_arr = []
                for row in trans_arr:
                    counter = Counter(row)
                    sortedlist = sorted(list(counter.items()), key=lambda x: (x[1], x[0]))
                    nrow = []
                    for s in sortedlist:
                        if s[0] == 0:
                            continue
                        nrow += [s[0]]
                        nrow += [s[1]]
                    tmp_arr += [nrow[:100]]
                    R = max(R, len(nrow))
                # full by zero
                for row in tmp_arr:
                    for _ in range(R-len(row)):
                        row += [0]

                tmp_arr = list(map(list, zip(*tmp_arr)))  # retransepose

                arr = deepcopy(tmp_arr)

            if 0 <= r < R and 0 <= c < C and arr[r][c] == k:
                print(t)
                return

    # t==0
    if 0 <= r < R and 0 <= c < C and arr[r][c] == k:
        print(0)
    else:
        calculate()
