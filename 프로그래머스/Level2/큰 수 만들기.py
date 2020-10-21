# 뺴되, 순서는 지켜야 한다가 핵심
# 투포인터 + 윈도우 생성으로 풀이 / 스택 개념으로봐도 무방

def solution(number, k):
    window = []
    s, e = 0, 1
    window.append(number[s])

    def fill_window(k, num, window):  # num이 window에서 자리를 찾아가도록
        while window and window[-1] < num and k>0: #  window[-1] >= number[e] 일 경우는 while문 안돈다.
            window.pop()
            k -= 1
        window.append(num)
        return k

    for e in range(1, len(number)):
        k = fill_window(k, number[e], window)
        if k==0:
            break

    window.extend(number[e + 1:])

    if k != 0: # '999' 반례를 위해
        while k != 0:
            k -= 1
            window.pop()

    return ''.join(window)