def solution(n, times):
    minv, maxv = min(times), max(times)

    # binary search
    answer = maxv * n
    start, end = 0, maxv * n
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for t in times:
            people += mid // t  # 6명 이상이어야 함. 중복 포함해서. 더 큰값 나와도 실제로는 6명일 수 있음

        if people >= n:
            # 줄인다.
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer