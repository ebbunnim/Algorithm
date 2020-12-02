import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = [([point[0]**2+point[1]**2] + point) for point in points]
        heapq.heapify(points)
        ans = []
        for _ in range(K):
            ans.append(heapq.heappop(points)[1:])
        return ans