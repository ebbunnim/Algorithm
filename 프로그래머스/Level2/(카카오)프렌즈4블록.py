from copy import deepcopy

def solution(m, n, board):
    for i in range(len(board)):
        board[i] = list(board[i])

    def bomb(x, y):
        for dx, dy in (1, 0), (0, 1), (1, 1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and board[x][y] == board[nx][ny]:
                pass
            else:
                return False
        return True

    def down():
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if board[i][j]=='1':  # 빈 공간이라
                    for a in range(i-1, -1,-1):
                        if board[a][j] != '1': # 빈 공간 아닐
                            board[i][j] = board[a][j] # 끌어내려
                            board[a][j] = '1'
                            break

    while True:
        flag = 0
        copy_board = deepcopy(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]!='1' and bomb(i, j):
                    copy_board[i][j] = '1'
                    copy_board[i+1][j]='1'
                    copy_board[i][j+1]='1'
                    copy_board[i+1][j+1]='1'
                    flag = 1
        if flag == 0:
            break
        else:
            board = deepcopy(copy_board)
            down()
    ans = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == '1':
                ans += 1
    return ans

