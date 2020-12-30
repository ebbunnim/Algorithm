def blank(r, c, height, width):
    if height == 3:
        arr[r + 1][c + 3] = ' '
        return
    # blank
    x = r + height // 2
    y = c + width // 4
    l = width // 2
    s = y
    for i in range(x, x + height):
        for j in range(s + 1, s + l):
            arr[i][j] = ' '
        l -= 2
        s += 1
    blank(r, c + width // 4, height // 2, width // 2)
    blank(r + height // 2, c, height // 2, width // 2)
    blank(r + height // 2, c + width // 2, height // 2, width // 2)

if __name__ == '__main__':
    N = int(input())
    arr = [['*']*(2*N) for _ in range(N)]
    width = (1+2*N)
    mid=width//2
    height=N
    i=0
    while i<N:
        for j in range(mid):
            if j==0:
                arr[i][j]=''
                continue
            arr[i][j]=' '
            arr[i][width-1-j]=' '
        mid-=1
        i+=1

    blank(0,0,height,width)

    for x in arr:
        print(''.join(x))