global ans
ans = 51


def next_word(word1, word2):
    res = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            res += 1
    return res


def solution(begin, target, words):
    if target not in words:
        return 0

    N = len(words)
    vis = [False] * N

    def dfs(start, cnt):
        global ans

        if start == target:
            if ans > cnt:
                ans = cnt
            return

        for i in range(len(words)):
            if next_word(start, words[i]) == 1 and vis[i] == False:
                vis[i] = True
                cnt += 1
                dfs(words[i], cnt)
                vis[i] = False
                cnt -= 1

    dfs(begin, 0)

    return ans
