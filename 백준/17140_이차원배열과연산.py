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
        global t, R, C, arr
        t += 1
        if t > 100:
            return -1

        if C>R: # C연산
            tmp_map =[]
            arr = list(map(list,zip(*arr)))
            for row in arr:
                counter = Counter(row)
                _tmp = sorted(list(counter.items()), key=lambda x: (x[1], x[0]))
                tmp = []
                for _t in _tmp:
                    if _t[0]==0:
                        continue
                    tmp.append(_t[0])
                    tmp.append(_t[1])
                row_len = len(tmp)
                R = max(R, row_len)
                tmp_map.append(tmp[:100])
            for tmp in tmp_map:
                for _ in range(R-len(tmp)):
                    tmp+=[0]
            tmp_map = list(map(list, zip(*tmp_map)))
        else: # R연산
            tmp_map = []
            for row in arr:
                counter = Counter(row)
                _tmp = sorted(list(counter.items()), key=lambda x : (x[1],x[0]))
                tmp = []
                for _t in _tmp:
                    if _t[0]==0:
                        continue
                    tmp.append(_t[0])
                    tmp.append(_t[1])
                col_len = len(tmp)
                C = max(C,col_len)
                tmp_map.append(tmp[:100])
            for tmp in tmp_map:
                for _ in range(C-len(tmp)):
                    tmp+=[0]

        # k 확인 & arr <- tmp_map
        if 0<=r<R and 0<=c<C and tmp_map[r][c]==k:
            return t
        arr = deepcopy(tmp_map)


    if 0<=r<R and 0<=c<C and arr[r][c]==k:
        print(0)
    else:
        while True:
            a = calculate()
            if a:
                break
        print(a)


    # 연산 진행후에는 k와 일치하는지 봐야함.
    # 등장횟수 카운트
    # 새로운 숫자가 있다면, 배열은 확장한다. 아니면 무시한다.
    # 새롭게 정렬한다.
    # 이때, 배열의 크기가 딕셔너리로 관리된다.
    # max R, C를 관리하면서 그 차이만큼 0으로 추가한다.
    # 각 행과 열마다 연산을 해줘야 한다.


