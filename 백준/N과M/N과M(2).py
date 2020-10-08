import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + 루트=>자식 제한. 루트보다 큰 수여야 한다(start 제한)
if __name__=="__main__":
    N,M = map(int, input().split())
    node = [str(i) for i in range(1,N+1)]
    vis = [False]*(N)

    res = []
    def dfs(cnt,res,start):
        if cnt == M:
            print(' '.join(res))
            return

        for n in range(start,N):
            if vis[n]==False:
                vis[n] = True
                res+=[node[n]]
                dfs(cnt+1,res,n+1)
                vis[n]=False
                res.pop()
    dfs(0,[],0)