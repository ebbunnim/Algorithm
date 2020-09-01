def solution(n):
    answer = []

    def hanoi(start, end, mid, pans, answer):
        if pans == 1:  # 1개만 남으면
            answer.append([start, end])
            return
        hanoi(start, mid, end, pans - 1, answer)
        answer.append([start, end])
        hanoi(mid, end, start, pans - 1, answer)

    hanoi(1, 3, 2, n, answer)  # from, to, mid, n개의 원반
    return answer