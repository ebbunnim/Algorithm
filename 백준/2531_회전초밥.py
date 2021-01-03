from collections import deque

if __name__ == '__main__':
    N,K,W,F = map(int,input().split())
    dishes=[int(input()) for _ in range(N)]
    maxv=0
    window = deque(dishes[:W])
    for i in range(N):
        l=len(set(window))
        if F not in window:
            l+=1
        if l>maxv:
            maxv=l
        window.popleft()
        window.append(dishes[(i+W)%N])
    print(maxv)