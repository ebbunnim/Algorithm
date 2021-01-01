# 블록게임 80% 맞은 코드 - 아래로 떨어뜨리는 것 말고 위로 막힌 블록 있는지 확인해서 해결했음

cnt = 0
def solution(board):
    global cnt
    N = len(board)

    def is_in_patterns(i, j, num):
        global cnt
        if (j + 2) < N and (i + 1) < N and board[i][j] == num and board[i + 1][j] == num and board[i + 1][
            j + 1] == num and board[i + 1][j + 2] == num and board[i][j + 1] == -1 and board[i][j + 2] == -1:
            board[i][j] = board[i + 1][j] = board[i + 1][j + 1] = board[i + 1][j + 2] = -1
            cnt += 1
            return 1
        if (j + 1) < N and 0 <= (i - 2) and board[i][j] == num and board[i][j + 1] == num and board[i - 1][
            j + 1] == num and board[i - 2][j + 1] == num and board[i - 1][j] == -1 and board[i - 2][j] == -1:
            board[i][j] = board[i][j + 1] = board[i - 1][j + 1] = board[i - 2][j + 1] = -1
            cnt += 1
            return 1
        if (j + 1) < N and (i + 2) < N and board[i][j] == num and board[i + 1][j] == num and board[i + 2][j] == num and \
                board[i + 2][j + 1] == num and board[i][j + 1] == -1 and board[i + 1][j + 1] == -1:
            board[i][j] = board[i + 1][j] = board[i + 2][j] = board[i + 2][j + 1] = -1
            cnt += 1
            return 1
        if (j + 2) < N and 0 <= (i - 1) and board[i][j] == num and board[i][j + 1] == num and board[i][j + 2] == num and \
                board[i - 1][j + 2] == num and board[i - 1][j] == -1 and board[i - 1][j + 1] == -1:
            board[i][j] = board[i][j + 1] = board[i][j + 2] = board[i - 1][j + 2] = -1
            cnt += 1
            return 1
        if (j + 2) < N and 0 <= (i - 1) and board[i][j] == num and board[i][j + 1] == num and board[i - 1][
            j + 1] == num and board[i][j + 2] == num and board[i - 1][j] == -1 and board[i - 1][j + 2] == -1:
            board[i][j] = board[i][j + 1] = board[i - 1][j + 1] = board[i][j + 2] = -1
            cnt += 1
            return 1
        return 0

    for j in range(N):
        for i in range(N):
            if board[i][j] != 0:
                break
            board[i][j] = -1
    while True:
        flag = 0
        for j in range(N):
            for i in range(N):
                if board[i][j] >= 1:
                    flag += is_in_patterns(i, j, board[i][j])
        if flag == 0:
            break

        for j in range(N):
            for i in range(N):
                if board[i][j] >= 1:
                    break
                board[i][j] = -1
    return cnt
