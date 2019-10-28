import sys
sys.stdin = open("input.txt", "r")

def matprint(arr):
    for i in range(len(arr)):
        print(arr[i])

def notwall(new_x, new_y):
    return 0 <= new_x < N and 0 <= new_y < N

# 시작이 0일때가 문제
def iszero_1(x, y): #right, left에 한해서 행을 가져온다면,
    if dir[0] == 1: mydir = N
    elif dir[0] == -1: mydir = -1

    for i in range(y, mydir,dir[0]): # 왼쪽이면 dir[0]=1, 오른쪽이면 dir[0]=-1
        while notwall(x, i + dir[0]):
            if arr[x][i+ dir[0]] == 0:
                i += dir[0]
            elif arr[x][i + dir[0]] != 0:
                arr[x][y] = arr[x][i + dir[0]]
                arr[x][i + dir[0]] = 0 # 어차피 arr[x][y]와 똑같을 것.
                break
    return arr

def iszero_2(x, y):
    while notwall(x+dir[0], y):
        arr[x][y] = arr[x+dir[0]][y]
        x += dir[0]
    arr[x][y] = 0
    return arr

def move_1(dir):
    global arr
    for x in range(N):
        for y in range(N):
            # 0을 만나면 옮기고, 수합치기까지 진행
            if arr[x][y] == 0:
                arr = iszero_1(x, y)
                # if notwall(x, y+dir[1]):
                #     if arr[x][y] == arr[x][y+dir[1]]:
                #         temp = arr[x][y] + arr[x][y+dir[1]]
                #         arr[x][y+dir[1]] = temp
                #         arr[x][y] = 0
            else: # 0이 아닌 수를 만나면, 오른편을 탐색하자
                if notwall(x, y+dir[1]):
                    if arr[x][y] == arr[x][y+dir[1]]:
                        temp = arr[x][y] + arr[x][y+dir[1]]
                        arr[x][y] = 0
                        arr[x][y+dir[1]] = temp # 진행방향에 해당 수를 놓는다.
                        # arr = iszero_1(x, y)
    return arr


def move_2(dir):
    global arr
    for y in range(N):
        for x in range(N):
            if (x, y) in visited:
                continue
            if arr[x][y] == 0:
                arr = iszero_2(x, y)
                if notwall(x+dir[1], y):
                    if arr[x][y] == arr[x+dir[1]][y]:
                        temp = arr[x][y] + arr[x+dir[1]][y]
                        arr[x+dir[1]][y] = temp
                        arr[x][y] = 0
                        arr = iszero_2(x, y)
                        visited.append((x+dir[1], y))
            else: # 0이 아닌 수를 만나면, 오른편을 탐색하자
                if notwall(x+dir[1], y):
                    if arr[x][y] == arr[x+dir[1]][y]:
                        temp = arr[x][y] + arr[x+dir[1]][y]
                        arr[x+dir[1]][y] = temp
                        arr[x][y] = 0
                        arr = iszero_2(x, y)
                        visited.append((x+dir[1], y))
    return arr




if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        N, where = input().split()
        N = int(N)
        arr = [0]*N
        for i in range(N):
            arr[i] = list(map(int, input().split()))

        visited = []

        # 행 기준
        if where == 'up':
            dir = [1, -1]  # zero, 미는
            result = move_2(dir)
        elif where == 'down':
            dir = [-1, 1]
            result = move_2(dir)

        elif where == 'left':
            dir = [1, -1]
            result = move_1(dir)
        elif where == 'right':
            dir = [-1, 1]
            result = move_1(dir)

        print('#%d' % tc)
        for i in range(N):
            temp = result[i]
            string = ''
            for t in temp:
                string += str(t)
                string += ' '
            print(string)