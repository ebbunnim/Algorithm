def blank(k):
    if k==0:
        return
    x=y=l=3**(k-1)
    for i in range(x,N,l*3):
        for j in range(y,N,l*3):
            for r in range(i,i+l):
                for c in range(j,j+l):
                    arr[r][c]=' '
    blank(k-1)

if __name__ == '__main__':
    N = int(input())
    arr=[['*']*N for _ in range(N)]
    k=1
    while True:
        if (3**k)==N:
            break
        k+=1
    blank(k)
    for x in arr:
        print(''.join(x))
