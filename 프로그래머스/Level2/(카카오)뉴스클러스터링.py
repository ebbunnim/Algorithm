from string import ascii_uppercase
from math import floor


def solution(str1, str2):
    def make_group(x):
        group = []
        for i in range(len(x) - 1):
            if x[i] not in ascii_uppercase:
                continue
            if x[i + 1] not in ascii_uppercase:
                continue
            group.append(x[i:i + 2])
        return group

    str1 = str1.upper()
    str2 = str2.upper()
    group1 = make_group(str1)
    group2 = make_group(str2)
    vis1 = [False] * len(group1)
    vis2 = [False] * len(group2)
    for i in range(len(group1)):
        for j in range(len(group2)):
            if vis2[j] != True and group1[i] == group2[j]:  # 1 / 1 1 이렇게 중복될 수 있다. intersect은 1에 대해서만 중복해야, 1 1 둘다 처리하면 안
                vis1[i] = True
                vis2[j] = True
                break
    # True인 애들은 공통적으로 교집합
    union_val = 0
    intersect_val = 0
    for v in vis1:
        if v == True:
            intersect_val += 1
        else:
            union_val += 1
    for v in vis2:
        if v == False:
            union_val += 1
    if intersect_val + union_val == 0:
        return 65536
    else:
        return floor((intersect_val / (union_val + intersect_val)) * 65536)

