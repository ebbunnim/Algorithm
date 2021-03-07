import sys
from itertools import combinations
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,K=map(int,input().split())
    words=[set(input().strip()[4:-4]) for _ in range(N)]
    vis=[False]*26
    pre_char={'a','n','t','i','c'}
    for c in pre_char:
        vis[ord(c)-97]=True
    candidates=set()
    for word in words:
        for c in (word-pre_char):
            candidates.add(c)
    print(candidates)
    if K<5:
        print(0)
    else:
        S=K-5
        for i in range(S+1):
            combs=list(combinations(candidates,i))
            for comb in combs:
                for word in words:
                    if word.difference(comb):
                        break


