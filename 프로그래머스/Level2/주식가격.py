def solution(prices):
    L = len(prices)
    ans = [0] * L
    stack = [0]  # 인덱스 관리

    for i in range(1, L):
        if prices[i] >= prices[stack[-1]]:
            stack += [i]
            continue
        while stack and prices[stack[-1]] > prices[i]:
            before = stack.pop()
            ans[before] = (i - before)
        stack += [i]

    if stack:
        terminal = stack[-1]
    for i in range(L):
        if ans[i] == 0:
            ans[i] = (terminal - i)

    return ans