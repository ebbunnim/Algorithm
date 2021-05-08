import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def union(x,y):
    x=find(x)
    y=find(y)
    parents[y]=x

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

if __name__ == '__main__':
    T=int(input().strip())
    for _ in range(T):
        N=int(input().strip())
        parents=list(range(N))
        xpos=[0 for i in range(N)]
        ypos=[0 for i in range(N)]
        radius=[0 for i in range(N)]
        for i in range(N):
            y,x,r=map(int,input().split())
            ypos[i]=y
            xpos[i]=x
            radius[i]=r
        ans=N
        for i in range(N):
            for j in range(i+1,N):
                ydif = ypos[i] - ypos[j]
                xdif = xpos[i] - xpos[j]
                r = radius[i] + radius[j]
                if (ydif * ydif + xdif * xdif) <= (r * r):
                    if find(i) != find(j):
                        union(i,j)
                        ans-=1
        print(ans)
