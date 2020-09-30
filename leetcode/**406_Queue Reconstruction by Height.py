import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 그리디한 정렬 => 우선순위큐
        # y가 의미하는, 내 앞에 몇개의 원소가 필요하다는 정보 중요
        # 그렇다면, 큰 애(x')를 먼저 위치시킨 후, 작은 애(x'')가 y를 충족시키게 x'를 밀어내야.
        # 더 작은 값이 들어오므로, x'의 y에는 영향을 주지 않는다.(영향이 있는 애부터 처리한게 핵심!)
        res = []
        heap = [[-p[0], p[1]] for p in people]
        heapq.heapify(heap)

        while heap:
            curr = heapq.heappop(heap)
            res.insert(curr[1], [-curr[0], curr[1]])
        return res

