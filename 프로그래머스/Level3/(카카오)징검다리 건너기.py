def solution(stones, k):
    s, e = 1, 200000000
    while s<=e:
        m = (s+e)//2
        cnt = 0
        maxv = 0
        # 0이 몇 개 연이어 있는지 확인
        for i in range(len(stones)):
            if (stones[i]-m)<=0:
                cnt += 1
                continue
            else:
                maxv = max(maxv, cnt)
                cnt = 0
        maxv = max(maxv, cnt)
        if maxv >= k:
            e = m-1
            answer = m
        else:
            s = m+1
    return answer