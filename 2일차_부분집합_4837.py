
T = int(input())

for test in range(1, T+1):

    N, K = map(int, input().split())

    arr = [i for i in range(1,13)]
    n = len(arr)

    l=''; l_2=[]
    for i in range(1<<n):  #2^n제곱 - 모든 부분집합 만들겠다
        for j in range(n):
            if i&(1<<j):
                l += str(arr[j])
        l += '/'

    #print(l)
    target=''
    for t in l:
        if t == '/':
            l_2.append(target)
            target=''
        else:
            target += t
    l_2.append(target)
    #print(l_2)

    sum_v=0; count=0
    for i in l_2:
        if len(i) == N:
            for j in i :
                sum_v += int(j)
            if sum_v == K:
                count+=1

    print('#%d %d' % (test, count))

