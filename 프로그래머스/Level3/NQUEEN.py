ans = 0

def solution(n):
    global ans
    cols = [0] * n

    def go(row):
        global ans

        if row == n:
            ans += 1
            return
        # 인덱스는 행, 값은 열의 위치값
        for i in range(n):  # 열을 순회함.
            cols[row] = i
            if check(i, row):
                go(row + 1)

    def check(col, row):
        for i in range(row): # 다른 행들이 같은 열을 가지고 있는지 봐야 됨. 이때 행은 지나온 행들에 한해서
            if cols[i] == col:  # 이 행에서 열이 중복된다면,
                return False
            if abs(col - cols[i]) == abs(row - i):  # 가로 == 세로
                return False
        return True

    go(0)
    return ans

print(solution(4))