if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        patterns = [input() for _ in range(N)]
        patterns.sort()
        flag = 'YES'
        for i in range(1,N):
            if patterns[i-1] in patterns[i][:len(patterns[i-1])]:
                flag = 'NO'
                break
        print(flag)
