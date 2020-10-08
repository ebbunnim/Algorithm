import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열  +  노드 중복 가능  (중복순열)  + start idx 제어함
if __name__=="__main__":
    N,M = map(int, input().split())
    node = [str(i) for i in range(1,N+1)]

    def dfs(cnt,res,start):
        if cnt == M:
            print(' '.join(res))
            return

        for n in range(start,N): # 순회 노드들. 루트 -> 자식 -> 자식... 순서가 있음. 상위노드로 돌아간 뒤 자식 없으면 루트노드가 독립적으로 바뀜.
            if res and res[-1]>node[n]:
                continue
            res+=node[n]
            dfs(cnt+1,res,start)
            res.pop()

    dfs(0,[],0)