import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + 나온 '결과값'들 중복되지 않게 관리(string변환 주의) + start idx 제어
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split()))
    node.sort()
    node = list(map(str, node))
    vis = [False]*N
    results = []
    def dfs(cnt,res,start):
        global results
        if cnt ==M:
            tmp = ' '.join(res)
            if tmp not in results:
                results+=[tmp]
                print(tmp)
            return

        for n in range(start,N):
            if vis[n]==False:
                vis[n]=True
                res+=[node[n]]
                dfs(cnt+1,res,n+1)
                vis[n] = False
                res.pop()

    dfs(0,[],0)

