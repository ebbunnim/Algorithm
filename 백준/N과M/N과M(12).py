import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + 나온 '결과값'들 중복되지 않게 관리(string변환 주의) +  원소 중복 사용 가능 + start idx 제어
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split()))
    node.sort()
    results = set()

    def dfs(cnt,res,start):
        if cnt==M:
            results.add(tuple(res))
            return

        for n in range(start,N):
            res+=[node[n]]
            dfs(cnt+1,res,n)
            res.pop()
    dfs(0,[],0)

    for r in sorted(results):
        print(' '.join(map(str,r)))