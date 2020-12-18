import re


def solution(dartResult):
    p = re.compile("([0-9]+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)
    ans = [0] * 3

    for i in range(3):
        ans[i] = int(scores[i][0])
        # bonus
        if scores[i][1] == 'S':
            ans[i] **= 1
        elif scores[i][1] == 'D':
            ans[i] **= 2
        else:
            ans[i] **= 3
        # option
        if scores[i][2] == '*':
            ans[i] *= 2
            if 0 <= i - 1 < 3:
                ans[i - 1] *= 2
        elif scores[i][2] == '#':
            ans[i] *= (-1)
    return sum(ans)