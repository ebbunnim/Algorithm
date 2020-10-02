import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')

from collections import defaultdict
# 정수. 반드시 a,b로 구성해야 한다.
if __name__ == '__main__':
    T = int(input())
    A = int(input())
    Alist = list(map(int, input().split()))
    B = int(input())
    Blist = list(map(int, input().split()))


    # a 부분합 - 조합 개념
    subA = defaultdict(int)
    for i in range(A):
        sumv=0
        for j in range(i,A):
            sumv+=Alist[j]
            subA[sumv]+=1

    # b 부분합
    subB = defaultdict(int)
    for i in range(B):
        sumv = 0
        for j in range(i,B):
            sumv+=Blist[j]
            subB[sumv]+=1

    ans = 0
    for a in list(subA):
        ans += (subA[a]*subB[T-a])
    print(ans)