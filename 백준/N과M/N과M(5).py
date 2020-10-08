import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split())) # 문자로 받으면 '11'<'9'
    vis = [False]*N
    node.sort()
    node = list(map(str, node))

    def dfs(cnt,res):
        if cnt == M:
            print(' '.join(res))
            return

        for i in range(N):
            if vis[i]==False:
                vis[i] = True
                res+=[node[i]]
                dfs(cnt+1,res)
                res.pop()
                vis[i] = False
    dfs(0,[])
