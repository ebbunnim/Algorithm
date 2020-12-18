def solution(m, n, board):
    board = [list(x) for x in board]
    bomb_list = ['dummy']

    while bomb_list:
        # find starters
        bomb_list = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '.' and (board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]):
                    bomb_list += [(i, j)]
        # bomb
        for x, y in bomb_list:
            board[x][y] = board[x + 1][y] = board[x][y + 1] = board[x + 1][y + 1] = '.'

        # relocate
        for i in range(n):
            for j in range(m - 1, -1, -1):  # 행 우선순회
                if board[j][i] == '.':
                    for x in range(j - 1, -1, -1):
                        if board[x][i] != '.':
                            board[j][i], board[x][i] = board[x][i], board[j][i]
                            break

    return sum(x.count('.') for x in board)