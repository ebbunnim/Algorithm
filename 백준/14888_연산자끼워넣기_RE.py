import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    Nlist = list(map(int, input().split()))
    # + - * %
    tmp = list(map(int, input().split()))
    bohos = []
    for _ in range(tmp[0]):
        bohos.append('+')
    for _ in range(tmp[1]):
        bohos.append('-')
    for _ in range(tmp[2]):
        bohos.append('*')
    for _ in range(tmp[3]):
        bohos.append('%')

    vis = [False]*sum(tmp)
    S = sum(tmp)
    res = []
    def calculate(bohos):
        res=Nlist[0]
        for i in range(1,N):
            if bohos[i-1]=='+':
                res+=Nlist[i]
            elif bohos[i-1]=='-':
                res-=Nlist[i]
            elif bohos[i-1]=='*':
                res*=Nlist[i]
            elif bohos[i-1]=='%':
                if res < 0:
                    res = abs(res)//Nlist[i]
                    res = -res
                else:
                    res//=Nlist[i]
        return res


    minv = 1e9+1
    maxv = -1e9-1

    def dfs(cnt):
        global minv, maxv
        if cnt==S:
            # calcuate
            tmp_res = calculate(res)
            minv = min(minv, tmp_res)
            maxv = max(maxv, tmp_res)
            return

        for i in range(S):
            if vis[i]==False:
                vis[i]=True
                res.append(bohos[i])
                dfs(cnt+1)
                vis[i]=False
                res.pop()

    dfs(0)

    print(maxv)
    print(minv)

