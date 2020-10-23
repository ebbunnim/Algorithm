def solution(s):
    N = len(s)
    minv = N

    for wsize in range(N // 2, 0, -1):
        swindow = s[0:wsize]
        cnt = 1
        length = wsize  # 새로운 단어가 등장할 때 length를 더한다.
        for i in range(wsize, N, wsize):
            ewindow = s[i:i + wsize]  # i+wsize가 N을 넘어가면 알아서 남은 것만 슬라이싱 됨에 주의!
            if swindow == ewindow:
                cnt += 1
            else:  # 이전과 다르다
                if cnt != 1:  # 1이면 압축 숫자로 더하지 않는다.
                    length += len(str(cnt))  # 압축
                length += len(ewindow)  # 마지막에 슬라이싱 wsize아니어도 담김
                swindow = ewindow
                cnt = 1

        if cnt != 1:  # 같게 종료되면
            length += len(str(cnt))
        minv = min(length, minv)

    return minv
