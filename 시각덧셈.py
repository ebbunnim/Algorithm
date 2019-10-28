import sys
sys.stdin = open("input.txt","r")

#홀짝으로 접근 (홀수는 시각, 짝수는 분) 각각 더해야
#시각의 경우는 12이상이면 1부터 다시 시작이고
#분의 경우에는 60분이 넘어가면 1시간 추가 까지 됨

def time_add(a, b):
    if a + b >= 13:
        time = (a + b) - 12
    else: time = (a + b)
    return time

def minute_add(a, b, t):
    temp = a + b
    if temp >= 60:
        t += 1
        temp -= 60
    return t, temp

T=int(input())
for tc in range(1, T+1):
    l = list(map(int, input().split()))
    temp = minute_add(l[1], l[3], time_add(l[0], l[2]))
    time_v=temp[0];  minute=temp[1]
    print('#%d %d %d' % (tc, time_v, minute))


