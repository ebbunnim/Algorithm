from collections import defaultdict

def solution(record):
    res = []
    # 해시인데, 상태관리만 함
    D = defaultdict(str)
    for r in record:
        tmpr = r.split(' ')
        if tmpr[0] == 'Enter':
            D[tmpr[1]] = tmpr[2]
            res.append(('Enter', tmpr[1])) # id만 넣어둠
        elif tmpr[0] == 'Change':
            D[tmpr[1]] = tmpr[2]
        else: # leave
            res.append(('Leave', tmpr[1]))
    ans = ['']*len(res)
    cnt = 0
    for r in res:
        if r[0] == 'Enter':
            ans[cnt] = f"{D[r[1]]}님이 들어왔습니다."
        else:
            ans[cnt] = f"{D[r[1]]}님이 나갔습니다."
        cnt += 1
    return ans