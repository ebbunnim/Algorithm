def solution(n):
    arr = []
    D = [(1, 0), (0, 1), (-1, -1)]
    for i in range(1, n + 1):
        arr.append([0] * i + [-1] * (n - i))

    arr[0][0] = 1
    idx = x = y = 0
    num = 2
    target = ((1 + n) * n) // 2

    while True:
        nx = x + D[idx][0]
        ny = y + D[idx][1]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            idx = (idx + 1) % 3
        if num == target + 1:
            break

    ans = []
    for i in range(n):
        ans += [x for x in arr[i] if x != -1]
    return ans