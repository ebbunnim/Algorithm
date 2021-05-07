import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def union(a,b): # a,b는 노드 번호임
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
        nodes[a]|=nodes[b]
    else:
        parents[a]=b
        nodes[b]|=nodes[a]

def find(x): # 속한 부모 찾아 나서기
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

if __name__ == '__main__':
    N,M=map(int,input().split())
    T=list(map(int,input().split()))
    Tn,Tset=T[0],set(T[1:])
    parents = list(range(M))
    nodes=[set()]*M
    graph=[[] for _ in range(M)]
    for i in range(M):
        P=list(map(int,input().split()))
        Pn,Plist=P[0],P[1:]
        nodes[i]=set(Plist)

    for i in range(M):
        for j in range(M):
            if i==j:
                continue
            if nodes[i]&nodes[j]: # 교집합의 원소가 있다면
                union(i,j)

    cnt=0
    for group in set(parents):
        if nodes[group]&Tset:
            continue
        cnt+=parents.count(group)
    print(cnt)

