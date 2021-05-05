import sys
from collections import Counter
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__=="__main__":
    g,s=map(int,input().strip().split())
    W=input().strip()
    S=input().strip()
    l,r=0,g # 0,4이면 0~3까지 슬라이싱 됨. e가 s까지 가면 됨
    rule = Counter(W)
    window = Counter(S[l:r])
    cnt=0
    while True:
        if rule==window:
            cnt+=1
        window[S[l]]-=1
        window+=Counter()
        l+=1
        r+=1
        if r==s+1:
            break
        window[S[r-1]]+=1
    print(cnt)