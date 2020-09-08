from string import ascii_uppercase
from collections import defaultdict
def solution(msg):
    msg = list(msg)
    D = defaultdict()
    for i in range(1, 27):
        D[ascii_uppercase[i-1]] = i
    idx = 27
    wc = msg[0]
    ans = []
    for i in range(1, len(msg)):
        wc += msg[i] # 다음글자까지.
        if wc not in D:
            D[wc] = idx
            idx+=1
            ans.append(D[wc[:-1]])
            wc = msg[i] # 다음글자로 초기화한다.
        else: #있다면 그대로 간다.
            pass
    ans.append(D[wc])
    return ans