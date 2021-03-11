import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def buildTree(s_in,e_in,s_post,e_post):
    if s_in>=e_in or s_post>=e_post:
        return
    root=postorder[e_post-1]
    print(root,end=' ')
    idx=idxs[root]
    left_size=idx-s_in
    buildTree(s_in, idx, s_post, s_post+left_size)
    buildTree(idx+1, e_in, s_post+left_size, e_post-1) # 마지막 원소는 제외

if __name__ == '__main__':
    N=int(input())
    inorder=list(map(int,input().strip().split()))
    postorder=list(map(int,input().strip().split()))
    # 하나는 루트를 잡는 용도
    # 하나는 분할 정복하며, 트리를 복원하는 용도
    idxs=[0]*(N+1)
    for idx,val in enumerate(inorder):
        idxs[val]=idx
    buildTree(0,N,0,N)


