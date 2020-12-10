import sys
sys.stdin = open('input.txt','r')

if __name__=="__main__":
    for t in range(10):
        N = int(input())
        Nlist = list(map(int,input().split()))
        ans=0
        for i in range(2,N-2):
            limit = max(Nlist[i - 1], Nlist[i - 2], Nlist[i + 1], Nlist[i + 2])
            if Nlist[i]-limit>0:
                ans+=Nlist[i]-limit
        print(f'#{t+1} {ans}')



