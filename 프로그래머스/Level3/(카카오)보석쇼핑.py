from collections import defaultdict


def solution(gems):
    D = defaultdict(int)
    gems_set = set(gems)
    N = len(gems_set)
    ans = []
    # N과 모든 D 채우면 같아져야 함
    cnt = 0
    s = 0
    for e in range(len(gems)):
        if D[gems[e]] == 0:
            cnt += 1
        D[gems[e]] += 1
        if cnt == N:
            ans.append([s + 1, e + 1])
            while s < e and D[gems[s]] - 1 != 0:
                D[gems[s]] -= 1
                s += 1
                ans.append([s + 1, e + 1])  # 더 짧아진 범위
            if D[gems[s]] - 1 == 0:
                D[gems[s]] -= 1
                cnt -= 1  # N개의 원소 중 하나가 삭제 되었다.
                s += 1
    ans.sort(key=lambda x: (x[1] - x[0]))
    return ans[0]

# 반례 주의 (끝까지 e 포인터 움직여야 하는 이유) ["DIA", "EM", "EM", "RUB", "DIA"] [3,5]