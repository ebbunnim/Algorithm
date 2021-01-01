cnt = 0
def solution(board):
    global cnt
    N = len(board)

    def is_in_patterns(i, j, num):
        global cnt
        if (j + 2) < N and (i + 1) < N and board[i][j] == num and board[i + 1][j] == num and board[i + 1][
            j + 1] == num and board[i + 1][j + 2] == num and board[i][j + 1] == 0 and board[i][j + 2] == 0:
            if is_possible(i, j+1) and is_possible(i, j+2):
                board[i][j] = board[i + 1][j] = board[i + 1][j + 1] = board[i + 1][j + 2] = 0
                cnt += 1
                return 1
        if (j + 1) < N and 0 <= (i - 2) and board[i][j] == num and board[i][j + 1] == num and board[i - 1][
            j + 1] == num and board[i - 2][j + 1] == num and board[i - 1][j] == 0 and board[i - 2][j] == 0:
            if is_possible(i-1, j) and is_possible(i-2, j):
                board[i][j] = board[i][j + 1] = board[i - 1][j + 1] = board[i - 2][j + 1] = 0
                cnt += 1
                return 1
        if (j + 1) < N and (i + 2) < N and board[i][j] == num and board[i + 1][j] == num and board[i + 2][j] == num and \
                board[i + 2][j + 1] == num and board[i][j + 1] == 0 and board[i + 1][j + 1] == 0:
            if is_possible(i, j+1) and is_possible(i+1, j+1):
                board[i][j] = board[i + 1][j] = board[i + 2][j] = board[i + 2][j + 1] = 0
                cnt += 1
                return 1
        if (j + 2) < N and 0 <= (i - 1) and board[i][j] == num and board[i][j + 1] == num and board[i][j + 2] == num and \
                board[i - 1][j + 2] == num and board[i - 1][j] == 0 and board[i - 1][j + 1] == 0:
            if is_possible(i-1, j) and is_possible(i-1, j+1):
                board[i][j] = board[i][j + 1] = board[i][j + 2] = board[i - 1][j + 2] = 0
                cnt += 1
                return 1
        if (j + 2) < N and 0 <= (i - 1) and board[i][j] == num and board[i][j + 1] == num and board[i - 1][
            j + 1] == num and board[i][j + 2] == num and board[i - 1][j] == 0 and board[i - 1][j + 2] == 0:
            if is_possible(i-1, j) and is_possible(i-1, j+2):
                board[i][j] = board[i][j + 1] = board[i - 1][j + 1] = board[i][j + 2] = 0
                cnt += 1
                return 1
        return 0


    def is_possible(i,j):
        while 0<=i-1:
            if board[i-1][j]!=0:
                return False
            i-=1
        return True
    while True:
        flag = 0
        for j in range(N):
            for i in range(N):
                if board[i][j] >= 1:
                    flag += is_in_patterns(i, j, board[i][j])
        if flag == 0:
            break

    return cnt

board=[[0, 0, 1, 1], [0, 0, 2, 1], [2, 2, 2, 1], [2, 0, 0, 0]]
print(solution(board))