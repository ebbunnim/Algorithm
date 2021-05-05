import sys
sys.stdin = open('input.txt','r')

def move(r,c):
    for r in range(H):
        if arr[r][c]==1 and not vis[r][c]: # c+1, c-1으로 두 번으로 나가야 한다.
            if 0<=c-1<N-1:
                pass
            else:
                pass

    return

# backtrackin by target_num (add 1 in given position)
def backtracking(cnt:int,target:int)->bool:
    # basis - cnt==target
    # pruning - 갈 수 없는 경우 ()
    # 1로 바꿔가면서 할 수 있지만, - move의 경우에는 col 지키면서 아래로 가다가, 1만나면 내려가는 구조
    return # True - 찾을 수 있다. False- 찾을 수 없다.

def bs()->int:
    s,e=0,(N-1)*H
    while s<=e:
        mid=(s+e)//2
        # backtracking in mid num -> 다 만족한다면,
        if backtracking(mid):
            e=mid
        else:
            s=mid+1
    return e # target 값을 넘겨야 하는지, 아니면 e값을 lower bound처럼 넘겨도 되는지 모르겠음.

if __name__ == '__main__':
    N,M,H=map(int,input().split())
    arr=[[0]*(N-1) for _ in range(H)]
    vis=[[False]*(N-1) for _ in range(H)]
    for _ in range(M):
        a,b=map(int,input().split())
        arr[a-1][b-1]=1
    print(*arr,sep='\n')



