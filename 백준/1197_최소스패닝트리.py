import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    V, E = map(int, input().split())
    # edges, parent 정보를 활용한다.
    edges = []
    for _ in range(E):
        n1,n2,c = map(int, input().split())
        edges.append((c,n1,n2))
    edges.sort() # 비용이 작은 것부터 순회

    parent = [0]*(1+V)
    for i in range(1,1+V):
        parent[i] = i

    def find_parent(parent, x):
        if parent[x]!=x:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]
    def union_parent(a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a < b :
            parent[b] = a
        else:
            parent[a] = b
    ans=0
    for edge in edges:
        c,n1,n2 = edge
        if find_parent(parent,n1) != find_parent(parent,n2):
            union_parent(n1,n2)
            ans += c
    print(ans)





