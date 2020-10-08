import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열
if __name__=="__main__":
    N,M = map(int, input().split())
    node = [str(i) for i in range(1,N+1)]
    vis = [False]*(N)
    res = []
    def dfs(res,cnt):
        if cnt == M:
            print(' '.join(res))
            return
        for n in range(N):
            if vis[n]==False:
                vis[n]=True
                res += [node[n]]
                dfs(res,cnt+1)
                vis[n]=False
                res.pop()
        return
    dfs([],0)