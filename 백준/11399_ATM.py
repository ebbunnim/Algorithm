if __name__ == '__main__':
    ans = 0
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()
    for i in range(n):
        for j in range(i+1):
            ans += n_list[j]
    print(ans)