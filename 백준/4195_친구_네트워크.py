import sys
from collections import defaultdict
input=sys.stdin.readline

def find_parent(x):
    if parent_dict[x]!=x:
        parent_dict[x]=find_parent(parent_dict[x])
    return parent_dict[x]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a != b:
        parent_dict[b]=a
        cnt_parent[a]+=cnt_parent[b]

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        F=int(input())
        parent_dict = defaultdict(str)
        cnt_parent=defaultdict(lambda:1)
        for _ in range(F):
            n1,n2=input().strip().split()
            if parent_dict[n1]=='':
                parent_dict[n1]=n1
            if parent_dict[n2]=='':
                parent_dict[n2]=n2
            union_parent(n1,n2)
            print(cnt_parent[find_parent(n1)])

