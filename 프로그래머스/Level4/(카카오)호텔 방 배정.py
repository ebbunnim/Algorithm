from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    def find_parent(vis, x):
        if vis[x] in vis: # 값이 다른 키로 연결된다면, 더 찾아가야 한다.
            vis[x] = find_parent(vis, vis[x])
        return vis[x]
    vis = defaultdict()
    for i in range(len(room_number)):
        if room_number[i] in vis:
            _v = find_parent(vis,room_number[i]) # 이 공간이 마지막으로 비어있으므로 배치하면 된다.
            room_number[i] = _v
            vis[_v] = _v + 1
        else:
            vis[room_number[i]] = room_number[i]+1 # 비어있는 다음 공간
    return room_number