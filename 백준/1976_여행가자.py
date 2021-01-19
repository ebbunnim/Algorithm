import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline

def union_parent(a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

if __name__ == '__main__':
    N=int(input())
    M=int(input())
    parent=[x for x in range(N)]
    arr=[list(map(int,input().split())) for _ in range(N)]
    course=list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                union_parent(i,j)

    res=set([find_parent(parent,c-1) for c in course])
    if len(res)==1:
        print('YES')
    else:
        print('NO')