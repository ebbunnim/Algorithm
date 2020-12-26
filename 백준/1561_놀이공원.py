def cnt_people_at_time(t):
    people=0
    for p in play_times:
        people+=(t//p)
    return people

def binary_search():
    s, e = 0, 2000000000*max(play_times) # 최악의 시간
    while s<e:
        t = (s+e)//2
        if cnt_people_at_time(t)>=N:
            e = t
        else:
            s = t+1
    return e

if __name__ == '__main__':
    N,M = map(int,input().split())
    play_times = list(map(int,input().split()))
    if N<=M:
        print(N)
    else:
        N -= M
        t = binary_search()
        people_at_before_t = cnt_people_at_time(t-1)
        cycle = (N-people_at_before_t)
        for idx,p in enumerate(play_times):
            if not t%p:
                cycle-=1
                if cycle==0:
                    print(idx+1)
                    break