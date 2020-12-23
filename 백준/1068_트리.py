def remove_node(removal):
    parents[removal] = -1
    for i in range(N):
        if parents[i] == removal:
            remove_node(i)
    return

if __name__ == '__main__':
    N = int(input())
    parents = list(map(int, input().split()))
    removal = int(input())
    graph = [[] for _ in range(N)]

    # make graph
    for i in range(N):
        if parents[i]==-1:
            root=i
            continue
        graph[i]+=[parents[i]]
        graph[parents[i]]+=[i]

    # remove nodes & collect left nodes
    remove_node(removal)
    leaves=[]
    sets=set()
    for idx, num in enumerate(parents):
        if num!=-1:
            leaves+=[(idx,num)]
            sets.add(num)

    cnt=0
    if leaves==[] and removal!=root:
        print(1)
    else:
        for ele in leaves:
            if ele[0] not in sets:
                cnt+=1
        print(cnt)
