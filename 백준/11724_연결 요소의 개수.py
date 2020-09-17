import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N,M = map(int, input().split())
    parent = [0]*(1+N)
    for i in range(1,N+1):
        parent[i] = i
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x : min(x))

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    def union_parent(a, b): # 부모가 다르다면, 합치게 도와준다.
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a < b: # 더 작은 노드 번호로 갱신하겠다.
            parent[b] = a
        else:
            parent[a] = b

    for edge in edges:
        a, b = edge
        if find_parent(parent,a) != find_parent(parent, b):
            union_parent(a, b)
    parent.pop(0)
    print(len(set(parent)))




