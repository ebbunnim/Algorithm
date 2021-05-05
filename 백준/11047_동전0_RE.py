import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,K=map(int,input().split())
    coins=[int(input()) for _ in range(N)]
    cnt=0
    for i in range(N-1,-1,-1):
        coin=coins[i]
        if K//coin:
            q,r=divmod(K,coin)
            cnt+=q
            K=r
    print(cnt)