def binary_search(l):
    s, e = 0, N
    while s <= e:
        mid = (s + e) // 2
        sumv = sum([x for x in range(mid, mid + l)])
        if sumv < N:
            s = mid + 1
        elif sumv == N:
            return [x for x in range(mid, mid + l)]
        else:
            e = mid - 1
    return

if __name__ == '__main__':
    N,L = map(int,input().split())
    flag=0
    for l in range(L,101):
        tmp=binary_search(l)
        if tmp is not None:
            print(*tmp)
            flag=1
            break
    if flag==0:
        print(-1)