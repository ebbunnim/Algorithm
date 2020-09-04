from collections import deque

def solution(cacheSize, cities):
    Q = deque()
    ans = 0
    for city in cities:
        city = city.upper()
        flag = 0
        if city in Q: # 이전 Q에서 있었다.
            flag = 1
        Q.append(city)
        if len(Q) > cacheSize:
            if flag == 0:
                Q.popleft()
                ans += 5
            else:
                Q.remove(city)
                ans += 1
        else:
            if flag == 1: # 교체
                Q.remove(city)
                ans += 1
            else:
                ans += 5
    return ans