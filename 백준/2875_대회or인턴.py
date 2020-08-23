if __name__ == '__main__':
    N,M,K = map(int,input().split())
    ans = 0

    while True:
        if K <= (N-2+M-1) and  N >=2 and M >=1:
            ans += 1
            N -= 2
            M -= 1
        else:
            break
    print(ans)
