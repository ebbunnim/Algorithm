import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,S,M = map(int, input().split()) # 곡수, 볼륨, 상한선
    diffs=list(map(int,input().split()))
    DP=[[0]*(1+M) for _ in range(N+1)]
    # DP[i][j] : 1이라면, i번째 곡에 체크된 볼륨
    DP[0][S]=1
    for i in range(N):
        for j in range(M+1):
            if DP[i][j]:
                if 0<=j+diffs[i]<=M:
                    DP[i+1][j+diffs[i]]=1
                if 0<=j-diffs[i]<=M:
                    DP[i+1][j-diffs[i]]=1
    ans=-1
    for i in range(M,-1,-1):
        if DP[N][i]:
            ans=i
            break
    print(ans)

