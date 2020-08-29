# 1. 간선정보들 - cost, node1, node2
# 2. parent - 자기자신으로 초기화, union_parent, find_parent

def solution(n, costs):
    ans = 0
    edges = []
    parent = [0]*n
    for i in range(n):
        parent[i] = i # 자기자신을 부모로 초기화
    for e in costs:
        edges.append((e[2], e[0], e[1])) # 비용, start_node, end_node

    edges.sort()


    def union_parent(parent, a, b):  # 같은 부모를 갖도록 합치겠다.
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a # 통상 더 작은 번호의 노드로 부모를 맞춰준다.
        else:
            parent[a] = b

    def find_parent(parent, x):
        if parent[x] != x: # 자기자신이 부모가 아니므로 현재 다른 노드를 부모로 갖는다. 최종적으로는 루트노드(자기 자체가 부모인)를 넣는다.
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b): # 같은 부모 가졌다면 사이클이 생겨서 안된다.
            union_parent(parent, a, b)
            ans += cost # 최소비용 누
    return ans
