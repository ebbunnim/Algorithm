import sys
sys.stdin = open('input.txt','r')

def union_parent(a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent, parent[x])
    return x

if __name__ == '__main__':
    N,M=map(int,input().split())
    edges=[]
    for _ in range(M):
        a,b,c=map(int,input().split())
        edges+=[(c,a,b)]
    edges.sort(key=lambda x : x[0])

    parent=[x for x in range(N+1)]
    mincost=0
    cnt=0
    for c,a,b in edges:
        if cnt==N-2:
            break
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(a,b)
            mincost+=c
            cnt+=1
    print(mincost)
