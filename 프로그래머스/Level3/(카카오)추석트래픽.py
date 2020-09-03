def solution(lines):
    def make_ms_sec(s): # ms 에 초점을 맞춤.
        s = s.split()
        during = s[2][:-1]
        t = s[1].split(':')
        hh = int(t[0])
        mm = int(t[1])
        tmp = t[2].split('.')
        ss = int(tmp[0]+tmp[1]) # ms 단위
        hh *= 1000
        mm *= 1000
        total_ms = hh*60*60 + mm*60 + ss
        if '.' in during:
            a, b = during.split('.')
        else:
            a, b = during, ''
        if len(b) == 3:
            during = int(a + b)
        else:
            during = int(a + b + '0'*(3-len(b)))

        return [total_ms-during+1, total_ms] # 시작시간, 끝시간
    def check(time):
        num = 0
        start = time
        end = time + 1000
        for dur in lines:
            if not (dur[1] < start or dur[0] >= end):
                num += 1
        ans.append(num)
        return
    # 1초는 1000 ms씩 옮겨간다.
    for i in range(len(lines)):
        lines[i] = make_ms_sec(lines[i])
    ans = []

    for line in lines:
        check(line[0])
        check(line[1])

    return max(ans)


# lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
#  "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
#  "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
#  "2016-09-15 21:00:02.066 2.62s"]
# print(solution(lines))