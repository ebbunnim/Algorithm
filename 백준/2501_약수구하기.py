import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,K=map(int,input().split())
    cnt=0
    ans=0
    for i in range(1,N+1):
        if not N%i:
            cnt+=1
            if cnt==K:
                ans=i
                break
    print(ans)