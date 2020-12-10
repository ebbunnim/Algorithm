import sys
sys.stdin = open('input.txt','r')


def dfs(x, y, cnt,tmp):
    if cnt==7:
        if tmp not in sets:
            sets.add(tmp)
        return

    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx = x + dx
        ny = y + dy
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx,ny,cnt+1,tmp+str(arr[nx][ny]))



if __name__=="__main__":
    for t in range(int(input())):
        arr = [list(map(int, input().split())) for _ in range(4)]
        sets = set()

        for i in range(4):
            for j in range(4):
                dfs(i,j,1,str(arr[i][j]))
        print(f'#{t+1} {len(sets)}')
