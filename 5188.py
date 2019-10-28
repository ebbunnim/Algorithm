import sys
sys.stdin = open("input.txt","r")

def notwall(new_x, new_y):
    return 0<=new_x<N and 0<=new_y<N

def DFS(x, y):
    global result, subresult
    dx=[1,0]; dy=[0,1]

    if result < subresult:
        return

    if x==N-1 and y==N-1:
        result = subresult
        return

    for i in range(2):
        new_x=x+dx[i]
        new_y=y+dy[i]
        if notwall(new_x, new_y) and (new_x, new_y) not in visited:
            visited.append((new_x, new_y))
            print(visited)
            subresult += arr[new_x][new_y]
            DFS(new_x, new_y)
            print('되돌아가자')
            visited.remove((new_x, new_y))
            subresult -= arr[new_x][new_y]





N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = list(map(int, input().split()))
print(*arr,sep='\n')
visited=[]
subresult=arr[0][0]; result=99999
DFS(0,0)
print(result)

# 0,0 -> N-1, N-1 까지 감
