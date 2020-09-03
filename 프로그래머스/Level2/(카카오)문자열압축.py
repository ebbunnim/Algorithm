def solution(s):
    def check(l):  # 자르는 문자열 길이
        cnt = len(s)
        for i in range(0, len(s), l):
            if i == 0:
                window = s[i:i + l]
                sub_cnt = 1
                continue
            if s[i:i + l] == window:  # 이전것과 같다면,
                cnt -= l
                sub_cnt += 1

            else:
                # 새롭게 윈도우를 잡는다.
                if i + l >= len(s):
                    break
                window = s[i:i + l]
                # sub_cnt = 10, 100, 1000 등 카운트 위해 len
                if sub_cnt >= 2:
                    cnt += len(str(sub_cnt))
                sub_cnt = 1  # 다시 처음으로 sub_cnt 갱신
        if sub_cnt != 1:  # 마지막 처리
            cnt += len(str(sub_cnt))
        return cnt

    ans = len(s)
    for i in range(1, len(s)):
        res = check(i)
        if ans > res:
            ans = res

    return ans