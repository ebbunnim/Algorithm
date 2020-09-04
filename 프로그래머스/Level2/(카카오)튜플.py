def solution(s):
    D = [0]*100001
    cnt = 0
    num = ''
    for e in s: # 숫자의 자리수를 모두 무시해버리니까 주의
        if e == '{' or e=='}' or e==',' or e==' ':
            if num != '':
                if D[int(num)] == 0:
                    cnt += 1
                D[int(num)] += 1
            num = ''
            continue
        else:
            num += e

    ans = []
    for i in range(cnt,0,-1):
        # print(D.index(i))
        ans.append(D.index(i))
    return ans