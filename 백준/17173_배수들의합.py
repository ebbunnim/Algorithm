import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')



if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    vis = [0]*(N+1)
    for M in nums:
        for i in range(1,N+1):
            if i%M==0:
                vis[i]=1
    ans=0
    for i in range(1,N+1):
        if vis[i]==1:
            ans+=i
    print(ans)
