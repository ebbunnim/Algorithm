if __name__ == '__main__':
    N = int(input())
    D = [0]*pow(10,6)+[0]
    for i in range(1,N+1):
        if i == 1:
            D[i] = 0
        elif i == 2:
            D[i] = 1
        elif i == 3:
            D[i] = 1
        else:
            if i % 3 == 0 and i % 2 == 0 :
                D[i] = min(D[i//3]+1,D[i//2]+1,D[i-1]+1)
            elif i % 3 == 0:
                D[i] = min(D[i//3]+1,D[i-1]+1)
            elif i % 2 == 0:
                D[i] = min(D[i//2]+1,D[i-1]+1)
            else:
                D[i] = D[i-1] + 1
    print(D[N])
