import re
from collections import Counter


def solution(str1, str2):
    p = re.compile("[a-zA-Z]{2}")
    l1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1)]
    l2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1)]
    c1 = Counter([x for x in l1 if p.findall(x)])
    c2 = Counter([x for x in l2 if p.findall(x)])

    if not c1 and not c2:
        return 65536

    intersection = [x for x in c1 if x in c2]
    intersect = sum([min(c1[x], c2[x]) for x in c1 if x in c2])
    union = sum([c1[x] for x in c1 if x not in intersection]) + sum([max(c1[x], c2[x]) for x in c1 if x in c2]) + sum(
        [c2[x] for x in c2 if x not in intersection])

    return (intersect * 65536) // union