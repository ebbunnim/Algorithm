import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    l = list(map(int, input().split()))
    max=l[0]
    for i in l:
        if i >= max:
            max = i
    min = l[0]
    for i in l:
        if i <= min:
            min = i
    l.remove(max)
    l.remove(min)
    result = sum(l)/8
    print('#%d %d' % (tc,round(result)))