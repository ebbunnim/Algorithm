from itertools import combinations
from collections import defaultdict
from bisect import bisect_left
import re

def solution(info, query):
    # refine info - key에는 magic 기호 '-'을 기준으로 조합 생성해 활용. value에는 해당하는 조합에 매칭되는 score를 list로 관리
    combs = []
    for i in range(5):
        combs += list(combinations(range(4), i))
    D = defaultdict(list)
    for i in info:
        res = i.split()
        for comb in combs:
            s = ''
            for x in range(4):
                if x in comb:
                    s += '-'
                else:
                    s += res[x]
            D[s] += [int(res[4])]

    # for binary search
    for key, value in D.items():
        D[key] = sorted(value)

    # refine query
    ans = [1] * len(query)
    for i in range(len(query)):
        q = re.sub('and', '', query[i])
        q = q.split()
        key = ''.join(q[:4])
        # q[4]의 lower bound를 찾아 활용 (target과 '같거나 큰' idx)
        ans[i] = len(D[key]) - bisect_left(D[key], int(q[4]))
    return ans