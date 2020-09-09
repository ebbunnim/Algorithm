def solution(n, build_frame):
    def isvalid():  # 열, 행, 종류
        for [x, y, a] in res:
            if a == 0:  # 기둥
                if y == 0 or [x - 1, y, 1] in res or [x, y, 1] in res or [x, y - 1, 0] in res:
                    continue
                else:
                    return False
            else:  # 보
                if [x, y - 1, 0] in res or [x + 1, y - 1, 0] in res or ([x + 1, y, 1] in res and [x - 1, y, 1] in res):
                    continue
                else:
                    return False
        return True

    res = []
    for frm in build_frame:
        x, y, a, b = frm
        if b == 0:  # 삭제
            if [x, y, a] in res:
                res.remove([x, y, a])
            if isvalid():
                continue
            else:
                res.append([x, y, a])
        else:  # 설치
            res.append([x, y, a])
            if isvalid():
                continue
            else:
                res.pop()
    res.sort()
    return res