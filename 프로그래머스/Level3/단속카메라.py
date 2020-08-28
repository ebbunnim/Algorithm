def solution(routes):
    routes.sort(key=lambda x : x[1])
    cnt = 1
    start = routes[0][1]
    for i in range(1,len(routes)):
        if routes[i][0] <= start:
            continue
        else:
            start = routes[i][1]
            cnt += 1    
    return cnt