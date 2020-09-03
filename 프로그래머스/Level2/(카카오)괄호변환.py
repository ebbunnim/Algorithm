def solution(p):
    def correct(s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        if stack == []:
            return True
        return False

    def make_u_w(x):
        cnt = 0
        u = ''
        for i in range(len(x)):
            if x[i] == '(':
                cnt += 1
                u += x[i]
            else:
                cnt -= 1
                u += x[i]
            if cnt == 0:
                break
        v = x[i + 1:]
        return u, v

    def solve(x):
        if x == '':
            return x
        u, v = make_u_w(x)
        if correct(u):
            return u + solve(v)
        else:
            # 빈 문자열 나올때까지 진행해라.
            tmp = '(' + solve(v) + ')'
            tmp2 = u[1:len(u) - 1]
            for i in range(len(tmp2)):
                if tmp2[i] == '(':
                    tmp += ')'
                else:
                    tmp += '('
            return tmp

    if correct(p):  # 빈 문자열도 얘가 처리
        return p

    return solve(p)