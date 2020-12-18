from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    t = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache += [city]
            t += 1
        else:
            cache += [city]
            t += 5
    return t