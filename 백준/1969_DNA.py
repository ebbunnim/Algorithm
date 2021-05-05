import sys
sys.stdin = open('input.txt','r')
from collections import Counter

if __name__ == '__main__':
    N,M = map(int, sys.stdin.readline().split())
    DNAS = [input() for _ in range(N)]
    ans=''
    # 빈도수 계산 & 알파벳 우선순위 적용
    for val in zip(*DNAS):
        counter=Counter(val)
        maxv=0
        max_key='Z'
        for key,val in counter.items():
            if val>maxv:
                maxv=val
                max_key=key
            elif val==maxv:
                max_key=key if key<max_key else max_key
        ans+=max_key
    # count
    cnt=0
    idx=0
    for val in zip(*DNAS):
        cnt+=sum([1 for ele in val if ele!=ans[idx]])
        idx+=1
    print(ans)
    print(cnt)