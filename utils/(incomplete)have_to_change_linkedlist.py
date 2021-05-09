def solution(n, k, cmd):  # n은 행의 개수, k는 현재 행의 위치
    del_stack = []
    flags = ['O'] * n
    curr = k
    jumps = [0] * n

    def down(curr, num):
        cnt = 0
        while cnt != num:
            if flags[curr + 1] == 'O':
                cnt += 1
            curr += 1
        return curr

    def up(curr, num):
        cnt = 0
        while cnt != num:
            if flags[curr - 1] == 'O':
                cnt += 1
            curr -= 1
        return curr

    def mix(curr):  # 다 x이런애들로 있는 경우
        fl = 0
        while True:
            curr += 1
            if curr == n:  # 벗어나면,
                fl = 1
                curr -= 1
                break
            if flags[curr] == 'O':
                return curr
        if fl:  # 마지막이었거나, 마지막까지 가도 다 삭제된 애들만 있을 경우
            while True:
                curr -= 1
                if flags[curr] == 'O':
                    return curr
        # 여기로 떨어지는 일은 없다고 함

    for c in cmd:
        res = c.split()
        if res[0] == 'D':  # 아래칸 선택
            curr = down(curr, int(res[1]))
        elif res[0] == 'U':  # 위에칸 선택
            curr = up(curr, int(res[1]))
        elif res[0] == 'C':  # 현재 삭제, 아래 선택 (더 아래가 없으면 위행 선택)
            flags[curr] = 'X'
            del_stack += [curr]
            curr = mix(curr)
        else:  # 가장 최근에 삭제한 행 복구
            recent_del_idx = del_stack.pop()
            flags[recent_del_idx] = 'O'
    answer = ''
    for flag in flags:
        answer += str(flag)
    return answer
n=8
k=2
cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n,k,cmd)