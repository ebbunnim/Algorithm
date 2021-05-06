import sys
sys.stdin = open('input.txt','r')

# 일단, 한 지점에 들어갈 수 없으면 앞쪽으로 계속 들어가서 붙인다.
def find_parent(x):
    if parents[x]==x: # 바로 도킹시킨다.
        return x
    else: # 도킹이 안된 앞쪽 끝까지 들어간다.
        parents[x]=find_parent(parents[x])
        return parents[x]

def union_parent(x,y):
    x=find_parent(x)
    y=find_parent(y)
    # check 1
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

if __name__=="__main__":
    G=int(input())
    P=int(input())
    parents=list(range(G+1))
    ans=0
    for _ in range(P):
        gate=int(input())
        parent=find_parent(gate)
        if parent==0:
            break
        ans+=1
        # check 2
        union_parent(parent,parent-1)
    print(ans)