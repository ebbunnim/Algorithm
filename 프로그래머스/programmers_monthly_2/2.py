def solution(s):
    rule = {
        ']': '[',
        ')': '(',
        '}': '{'
    }

    def check(_s):
        stack = []
        for e in _s:
            if e in close:
                stack.append(e)
            else:
                if stack:
                    if stack[-1] != rule[e]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

    opn = rule.keys()
    close = rule.values()
    # 첫번째는 열려 있어야 한다. 아니면 바로 안됨
    # 열려있다면, 닫혀야 하는데, 열린걸 계속 담다가 안닫히면 안됨.
    cnt = 0
    for _ in range(len(s)):
        cnt += check(s)
        s = s[1:] + s[0]
    return cnt