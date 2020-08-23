
import heapq

if __name__ == '__main__':

    N, K= map(int, input().split())
    jewelry = [list(map(int,input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]
    jewelry.sort()
    bags.sort()
    max_heap = []
    j = 0
    ans = 0

    # 무게 기준으로 정렬되었고, 가능한 모든 값들을 다 힙에 넣어야 함. pop해버리면 pop된 애들 중에 두번째로 큰 애가 있을 수도 있다.
    for i in range(K):
        while j<N and bags[i]>=jewelry[j][0]:
            heapq.heappush(max_heap, (-jewelry[j][1], jewelry[j][1]))
            j += 1

        # 고침
        if len(max_heap) > 0:
            b = heapq.heappop(max_heap)
            ans += abs(b[1])

    print(ans)
