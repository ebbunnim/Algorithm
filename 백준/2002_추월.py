
from collections import deque

if __name__ == '__main__':
    N = int(input())
    in_tunnel = deque()
    out_tunnel = deque()
    for _ in range(N):
        in_tunnel.append(input())
    for _ in range(N):
        out_tunnel.append(input())
    cnt = 0

    for i in range(N):
        cur = in_tunnel.popleft()  # 이렇게 하면, out엔 없는데 in엔 있어버리는 결과가 나옴. 그러면 out_tunnel[0]에 절대 걸릴 수가 없음.

        while True:

            if not out_tunnel:
                break

            if cur not in out_tunnel:
                break # in도 계속 빼줘야
            elif cur != out_tunnel[0]:
                out_tunnel.popleft()
                cnt += 1
            else:
                out_tunnel.popleft() # 같다고 한다면, 카운트 안하고 뺸다. 그리고 새롭게 cur을 찾으러 간다.
                break
    print(cnt)
