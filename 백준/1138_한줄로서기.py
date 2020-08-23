if __name__ == '__main__':
    n = int(input())
    n_list = list(map(int, input().split()))
    ans = [0]*n

    for i in range(n): # val 찾음
        cnt = 0
        for j in range(n): # cnt 찾음
            if ans[j] == 0:
                if cnt == n_list[i]:
                    ans[j] = i+1
                    break
                else:
                    cnt += 1

    for a in ans:
        print(a, end=' ')