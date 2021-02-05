import sys
sys.stdin = open('input.txt','r')

# 시작, 종료, 중복, 카운트, pruning, clean
# 루트 노드가 모두 독립적으로 호출됨 == 순열 + 나온 '결과값'들 중복되지 않게 관리(string변환 주의)
if __name__=="__main__":
    N,M = map(int, input().split())
    node = list(map(int, input().split())) # 문자로 받으면 '11'<'9'
    node.sort()
    node = list(map(str, node))
    vis = [False]*N
    results = []

    def dfs(cnt,res):
        global results
        if cnt==M:
            tmp = ' '.join(res)
            if tmp not in results:
                # print(id(res))
                results.append(tmp)
                print(tmp)
            return

        for n in range(N):
            if vis[n]==False:
                res+=[node[n]]
                vis[n] = True
                dfs(cnt+1,res)
                vis[n] = False
                res.pop()

    dfs(0,[])



# 스택을 사용하면 dfs에서 값이 바뀌면, results에서도 해당 객체가 수정되어 버림. mutable 객체이기 때문에
# 이때는 string 으로 바꿔서 불변 객체로 만든 뒤 results에 넣어야 함.
