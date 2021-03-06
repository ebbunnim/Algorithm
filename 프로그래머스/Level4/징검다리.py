# lower bound + max
def solution(distance, rocks, n):
    rocks.sort()

    def binary_search():
        s, e = 0, distance  # 돌을 다 제거했을 경우 max
        ans = s
        while s < e:
            mid = (s + e) // 2  # 값 자체를 타겟
            cnt = 0
            start = 0
            for rock in rocks:
                if rock - start < mid:
                    cnt += 1  # 제거
                else:
                    start = rock  # 제거되지 않은 바위로 start 바꿔줌
            if cnt > n:
                e = mid
            else:
                s = mid + 1
                ans = mid
        return ans

    return binary_search()