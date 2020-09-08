def solution(n, t, m, p):
    def convert(num, x): #num을 x진법으로 바꾼다.
        T = '0123456789ABCDEF'
        q, r = divmod(num,x)
        if q == 0:
            return T[r]
        else:
            return convert(q, x) + T[r]
    def make_list(cycle): # x진법으로 cycle자리수까지 이어 붙이기
        res = ''
        for i in range(t*m):
            res += convert(i, n)
            if len(res) >= cycle:
                return res
    cycle = t*m # 전체
    cycle_list = make_list(cycle)
    ans = ''
    for i in range(p-1,cycle,m):
        ans += cycle_list[i]
    return ans