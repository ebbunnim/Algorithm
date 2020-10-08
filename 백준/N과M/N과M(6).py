import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + start idx 제어
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split())) # 문자로 받으면 '11'<'9'
    vis = [False]*N
    node.sort()

    def dfs(cnt, res, start):
        if cnt == M:
            for r in res:
                print(r, end=' ')
            print()
            return
        for n in range(start,N):
            if vis[n] == False:
                vis[n] = True
                res+=[node[n]]
                dfs(cnt+1, res, n+1)
                res.pop()
                vis[n] = False
    dfs(0,[],0)