import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    print('#%d' % tc)
    N = int(input())
    temp=''
    for i in range(N):
        alpha, lenght = input().split()
        lenght = int(lenght)
        temp += alpha*lenght

    start = 0
    for i in range(len(temp)//10+1):
        end = (i+1)*10
        print(temp[start:end])
        start = end