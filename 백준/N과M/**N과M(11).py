import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + 나온 '결과값'들 중복되지 않게 관리(string변환 주의) +  원소 중복 사용 가능
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split()))
    node.sort()
    # node = list(map(str, node))
    results = set()

    def dfs(cnt,res):
        global results

        if cnt==M:
            tmp = tuple(res)
            # print(id(res))
            results.add(tmp) # 리스트는 넣을 수 없지만 튜플은 넣을수 있음
            return

        for n in range(N):
            res+=[node[n]]
            dfs(cnt+1,res)
            res.pop()

    dfs(0,[])

    for r in sorted(results):
        print(' '.join(map(str,r))) # 위에서 선언 말고 이렇게 해야


    # 리스트랑 튜플 되게 비슷해. 근데, immutable 한것 차이가 있다. set에 append 하는 것도 다르고

