import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + 중복가능
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split())) # 문자로 받으면 '11'<'9'
    node.sort()

    def dfs(cnt,res):
        if cnt == M:
            for r in res:
                print(r,end=' ')
            print()
            return

        for n in range(N):
            res+=[node[n]]
            dfs(cnt+1,res)
            res.pop()


    dfs(0,[])