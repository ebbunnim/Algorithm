def DP(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return DP(num-1) + DP(num-2) + DP(num-3)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        print(DP(N))