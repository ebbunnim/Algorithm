from math import ceil,log2
import sys
input=sys.stdin.readline

def init(node,s,e):
    if s==e:
        tree[node]=nodes[s]
        return tree[node]
    tree[node]=init(node*2,s,(s+e)//2)+init(node*2+1,(s+e)//2+1,e)
    return tree[node]


def query(node,s,e,l,r):
    if l>e or r<s:
        return 0
    if l<=s and e<=r:
        return tree[node]
    return query(node*2,s,(s+e)//2,l,r)+query(node*2+1,(s+e)//2+1,e,l,r)


def update(node,s,e,idx,delta):
    if idx<s or idx>e:
        return
    tree[node]+=delta
    if s!=e:
        update(node*2,s,(s+e)//2,idx,delta)
        update(node*2+1,(s+e)//2+1,e,idx,delta)


if __name__ == '__main__':
    N,M,K=map(int,input().split())
    H=int(ceil(log2(N)))
    tree=[0]*(1<<(H+1))
    nodes=[]
    for _ in range(N):
        nodes+=[int(input())]
    init(1,0,N-1) #node num, start idx, end idx
    for _ in range(M+K):
        a,b,c=map(int,input().split())
        if a==1:
            delta=c-nodes[b-1]
            nodes[b-1]=c
            update(1,0,N-1,b-1,delta)
        else:
            print(query(1,0,N-1,b-1,c-1))


"""
<세그먼트 트리 최대 크기>
N에 대한 세그먼트 트리의 최대 크기(포화 완전 이진 트리)를 구한다.
해당 구간을 담기 위한 트리 높이는 H(==int(ceil(log2(N)))), 포화완전이진트리에서의 모든 노드 개수는 2^(H+1)-1개가 된다.
https://www.acmicpc.net/blog/view/9
"""
