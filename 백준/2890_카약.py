
if __name__ == '__main__':
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]
    grade = 1
    vis =[0]*10
    for j in range(C-2,0,-1):
        flag = 0
        for i in range(R):
            if arr[i][j] != '.' and vis[int(arr[i][j])]==0:
                vis[int(arr[i][j])] = grade
                flag = 1
        if flag == 1:
            grade += 1
    for d in vis:
        if d != 0:
            print(d)