
from collections import Counter
#S = 'wreawerewa'
#pattern = 'wrea'
# 정답은 4개

S = 'tatatata'
pattern = 'ta'

s, e = 0, len(pattern)-1
counter = Counter(pattern)
pattern_keys = counter.keys()

window = Counter()

for ele in S[s:e+1]:
    if ele in pattern_keys:
        window[ele]+=1

ans = 0
while s<e and e<len(S):
    print(window)
    if window==counter:
        ans+= 1
        window[S[s]]-=1
        s += 1
        e += 1
        if e >= len(S):
            break
        window[S[e]]+=1
        continue
    else:
        # 패턴 외 다른 문자가 삽입된 경우
        if S[e] not in pattern_keys:
            s = e+1
            e += len(pattern)
            if e >= len(S):
                break
            window = Counter(S[s:e+1])
            continue
        else:   # 패턴 내 문자지만 등장 횟수가 달라진 경우
            window[S[s]] -= 1
            s += 1
            e += 1
            if e >= len(S):
                break
            window[S[e]] += 1

print(ans)