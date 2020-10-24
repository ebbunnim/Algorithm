import time
from collections import Counter
#S = 'wreawerewa'
#pattern = 'wrea'
# 정답은 4개

start = time.time()

S = 'aabaaabasfdsfadfsadfdffabbdfsdfsfabadsfdsfsdfabasdfdsfdsfdabaabasabababababababababababababababaa'
pattern = 'aab'
s, e = 0, len(pattern)-1
counter = Counter(pattern)
pattern_keys = counter.keys()

# method1 - faster
# ans=0
# wsize = len(pattern)
# for i in range(len(S)-wsize+1):
#     if Counter(S[i:i+wsize])==counter:
#         ans+=1
# print(ans)
# time : 0.0008871555328369141

#method2
window = Counter()

for ele in S[s:e+1]:
    if ele in pattern_keys:
        window[ele]+=1

ans = 0
while s<e and e<len(S):
    if window==counter:
        ans+= 1
        window[S[s]]-=1
        window += Counter()
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
            window+=Counter()
            s += 1
            e += 1
            if e >= len(S):
                break
            window[S[e]] += 1

print(ans)

# 시간 측정
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간





# 0인거 지워줘야 함. Counter의 경우에는 0 이 남잖아.
# 따라서 window+=Counter() 해줘야 아래 반례를 해결할 수 있음.
# S = 'absdfdsabsegdfbas'
# pattern = 'abs'



