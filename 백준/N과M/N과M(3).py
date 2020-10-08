import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열  + 노드 중복 가능  (중복순열)
if __name__=="__main__":
    N,M = map(int, input().split())
    node = [str(i) for i in range(1,N+1)]

    def dfs(cnt,res):
        if cnt == M:
            print(' '.join(res))
            return

        for n in range(N):
            res += node[n]
            dfs(cnt+1,res)
            res.pop()

    dfs(0,[])

    # Q. vis를 지웠는데도 무한루프 안뜨는 이유? M이 되었을 때 return 되면 방문하지 않은 하위 노드로 내려가기 때문.
    # 따라서 무한 루프가 돌 경우, (1)리턴 조건이 이상하거나 (2)global 변수가 이상할 가능성 높음.