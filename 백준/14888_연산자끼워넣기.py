def cal(a,b,boho):
    if boho == '+':
        return a + b
    elif boho == '-':
        return a - b
    elif boho == '*':
        return a * b
    else:
        if b == 0:
            return 0
        if a < 0 and b > 0:
            return -(abs(a)//b)
        return a // b

def dfs():
    global cnt, ans, max, min

    if cnt == N-1:
        copy_nums = [0] * N
        copy_nums[0] = nums[0]
        for j in range(1,N):
            res = cal(copy_nums[j-1],nums[j],ans[j-1])
            copy_nums[j] = res

        if res < min:
            min = res
        if res > max:
            max = res

        return

    for i in range(N-1):
        if vis[i] == False:
            vis[i] = True
            cnt += 1
            ans.append(bohos[i])
            dfs()
            vis[i] = False
            cnt -= 1
            ans.pop()


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int,input().split()))
    boho = list(map(int,input().split()))
    bohos = []
    vis = [False]*(N-1)
    copy_nums = [0]*N
    cnt = 0
    ans = []
    min, max = 1000000000,-1000000000
    # + - x %
    for i in range(4):
        if i == 0:
            for _ in range(boho[i]):
                bohos.append('+')
        elif i == 1:
            for _ in range(boho[i]):
                bohos.append('-')
        elif i == 2:
            for _ in range(boho[i]):
                bohos.append('*')
        else:
            for _ in range(boho[i]):
                bohos.append('%')

    dfs()
    print(max)
    print(min)