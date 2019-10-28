#0부터 좌표찍듯이
#부호 다르더라도 수가 같다면 같이 cnt에 넣기

import sys
sys.stdin = open("input.txt","r")

def abs_cnt(l, target):
    cnt = 0
    for i in range(len(l)):
        if l[i] == target:
            cnt += 1
    return cnt

def distance(l):
    for i in range(len(l)):
        if l[i] <= 0 :
            l[i] = -l[i]
    return l

def min(l): #list받아야
    min_v = l[0]
    for i in range(len(l)):
        if l[i] <= min_v:
            min_v = l[i]
    return min_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))

    # 절대값으로 환원
    min_v = min(distance(l))
    result = abs_cnt(distance(l), min_v)
    print('#%d %d %d' % (tc,min_v,result))