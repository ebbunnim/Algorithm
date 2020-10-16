import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    after_eat = 0
    N = len(food_times)
    for idx, val in enumerate(food_times):
        heapq.heappush(heap, (val, idx))

    while True:
        x = heapq.heappop(heap)
        k -= (x[0] - after_eat) * N
        if k <= 0:
            k += (x[0] - after_eat) * N
            heapq.heappush(heap, x)
            break
        after_eat = x[0]  # += 가 아니고 할당임.
        N -= 1

    heap.sort(key=lambda x: x[1])  # 다시 인덱스 순으로 배치
    return heap[k % N][1] + 1
