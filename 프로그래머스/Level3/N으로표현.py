ans = 9

def solution(N, number):
    D = [0] * 8  # 1부터 시작한 인덱스를 서로 더해서 8이 되면 됨
    for i in range(8):
        D[i] = int((i + 1) * str(N))

    def dfs(cnt, res, number):
        global ans
        if cnt > 8:
            return
        if res == number:
            if cnt < ans:
                ans = cnt
            return
        for i in range(8):
            ncnt = cnt + (i + 1)  # 이 개수만큼 사용한 요소를 사용하겠다.
            dfs(ncnt, res + D[i], number)
            dfs(ncnt, res * D[i], number)
            dfs(ncnt, res - D[i], number)
            dfs(ncnt, res / D[i], number)

    dfs(0, 0, number)
    if ans == 9:
        return -1
    else:
        return ans
