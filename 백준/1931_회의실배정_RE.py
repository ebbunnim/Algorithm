import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=[list(map(int,input().split())) for _ in range(N)]
    Nlist.sort(key=lambda x : (x[1],x[0]))
    ans=1
    e=Nlist[0][1]
    for i in range(1,N):
        if e<=Nlist[i][0]:
            ans+=1
            e=Nlist[i][1]
    print(ans)