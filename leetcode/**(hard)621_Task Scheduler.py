from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # n 간격 내에는 동일한 원소를 실행할 수 없다
        # 우선순위는 빈도수인데, n만큼은 lock 해버려야 함.
        # 빈도수를 기준으로 pop하되, 중복없이 n+1이 나올 수 있다면? 그러면 lock없이(no idle)  최대로 사용된 애를 붙일 수 있다.
        counter = Counter(tasks)
        res = []
        while True:
            heap = counter.most_common(n + 1) #Hack

            for h in heap:
                res += [h[0]]
                counter.subtract(h[0])
                counter += Counter()  # val==0일때 키값까지 제거

            if counter == {}: # no idle when finished
                break

            if 0 < len(heap) < (n + 1):
                for _ in range(n + 1 - len(heap)):
                    res += ['idle']
            else:
                continue

        return len(res)
