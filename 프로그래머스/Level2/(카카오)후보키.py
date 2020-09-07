from itertools import combinations

def solution(relation):
    def select(comb):
        res2 = []
        for i in range(len(relation)):
            res = []
            for c in list(comb):
                res.append(relation[i][c])
            res2.append(res)
        return res2

    M = len(relation[0])
    res = []
    for l in range(1, M + 1):
        combs = combinations([i for i in range(M)], l)
        for comb in combs:
            comb_list = select(comb)
            comb_list.sort()
            flag = 0
            for i in range(len(comb_list) - 1):
                if comb_list[i] == comb_list[i + 1]:
                    flag = 1
                    break
            if flag == 0:
                for e in res:
                    if set(comb).intersection(e) == e:  # 포함되어 있으면 안됨
                        flag = 2
                        break
                if flag != 2:
                    res.append(set(comb))
    return len(res)