def solution(n, times):
    # 최악의 시간을 찾고 -> 종료시간을 좁힌다. n을 근거로
    # n : lower bound가 됨
    def binary_search(n):
        s,e=0, max(times)*n
        while  s<e:
            mid = (s+e)//2 #종료시간
            people=0
            for t in times:
                people+=mid//t
            if people >= n: # lower bound
                e = mid
            else:
                s =  mid + 1
        return e
    return binary_search(n)