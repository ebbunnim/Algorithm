import sys
sys.stdin = open('input.txt','r')

from collections import Counter
if __name__=="__main__":
    for t in range(int(input())):
        N = int(input())
        Nlist = list(map(int,input().split()))
        counter = Counter(Nlist)
        print(f'#{t+1} {counter.most_common(1)[0][0]}')



