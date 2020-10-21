from collections import deque


def can_change(N, curr, nxt):
    cnt = 0
    for i in range(N):
        if curr[i] != nxt[i]:
            cnt += 1
            if cnt >= 2:
                return False
    return True  # 완벽하게 일치하는 경우는 없으므로 cnt!=0


def solution(begin, target, words):
    N = len(begin)
    vis = [False] * len(words)
    if target not in words:
        return 0

    # bfs 순회 조건은, ischange 하면,걔로 바꿔. 그리고 depth를 저장해라
    def bfs(begin, depth):
        Q.append((begin, depth))
        while Q:
            curr, depth = Q.popleft()
            if curr == target:
                return depth
            for i in range(len(words)):
                if vis[i] == False and can_change(N, curr, words[i]):
                    Q.append((words[i], depth + 1))
                    vis[i] = True
        return

    Q = deque()
    return bfs(begin, 0)