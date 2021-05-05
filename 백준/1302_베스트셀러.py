import sys
from collections import Counter
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N=int(input())
    Nlist=[input() for _ in range(N)]
    Nlist.sort()
    counter=Counter(Nlist)
    print(counter.most_common(1)[0][0])

