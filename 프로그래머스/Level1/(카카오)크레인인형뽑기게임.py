def solution(board, moves):
    stack = []
    answer = 0
    n = len(board)
    cnt = 0
    for col in moves:
        for row in range(n):
            if board[row][col - 1] == 0:
                continue

            if not stack:
                stack += [board[row][col - 1]]
            else:
                if stack[-1] == board[row][col - 1]:
                    stack.pop()
                    cnt += 2
                else:
                    stack += [board[row][col - 1]]
            board[row][col - 1] = 0
            break
    return cnt