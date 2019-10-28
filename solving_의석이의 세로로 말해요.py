import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1, T+1):
    arr = [0]*5
    max_len = 0
    for i in range(5):
        temp = input()
        arr[i] = temp #여기까지 넣어놓음
        l = [0] * max_len

        if len(temp) >= max_len:
            max_len = len(temp)


    for i in range(5):
        l = [''] * max_len #열의 공간
        mylist = []
        temp = arr[i]
        for a in arr[i]:
            mylist += a
        idx = 0
        while mylist:#열의 공간
            a = mylist.pop(0)
            l.insert(idx,a)
            l.pop()
            idx += 1

        arr[i] = l

    result = ''
    for i in range(max_len):
        for j in range(5):
            result += arr[j][i]
    print('#%d %s' % (tc, result))