import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=[]
    maxv=-1
    Nlist=[list(map(int,input().split())) for _ in range(N)]
    Nlist.sort()
    for i in range(N):
        if Nlist[i][1]>=maxv:
            maxv=Nlist[i][1]
            max_idx=i
    acc=maxv
    s=0
    for e in range(1,max_idx+1): # left
        if Nlist[s][1]<=Nlist[e][1]:
            acc+=Nlist[s][1]*(Nlist[e][0]-Nlist[s][0])
            s=e
    s=N-1
    for e in range(N-2,max_idx-1,-1): # right
        if Nlist[s][1]<=Nlist[e][1]:
            acc+=Nlist[s][1]*abs((Nlist[e][0]-Nlist[s][0]))
            s=e
    print(acc)
