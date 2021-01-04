import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    ans=0

    def dfs(curr,cnt,vis,res):
        global ans
        if cnt==N:
            if vis==(1<<10)-1:
                ans+=1
            return

        if DP[cnt][curr][vis]!='':
            return DP[cnt][curr][vis]
        # 234321 432121 => 얘를 똑같이 처리해버림.
        # 만약에 저렇게 한다면,

        # 첫번쨰 입력값 어떻게 받을거냐? 알 수가 없다.
        # 이후 연산함
        for delta in (-1,1):
            nxt=curr+delta
            if 0<=nxt<10 : # 들린적이 없다면?
                res=curr+dfs(nxt,cnt+1,vis|(1<<nxt),str(nxt))
        DP[cnt][curr][vis]=res

    for i in range(1,10):
        DP = [[['' for _ in range(1<<10)] for _ in range(10)] for _ in range(N)]  # len,0~9숫자,방문 집합
        dfs(i,0,(1<<i),str(i))

    print(ans%1000000000)