from collections import defaultdict

def solution(orders, course):
    def comb(sidx, order, s):
        D[s] += 1
        for i in range(sidx, len(order)):
            comb(i + 1, order, s + order[i])
        return

    D = defaultdict(int)
    for order in orders:
        comb(0, sorted(order), '')

    ans = defaultdict(list)
    for key, val in D.items():
        if (len(key) in course) and val >= 2:
            ans[len(key)] += [(val, key)]

    res = []
    for key in ans:
        maxv = max(ans[key])[0]
        res += [ele[1] for ele in ans[key] if ele[0] == maxv]

    return sorted(res)