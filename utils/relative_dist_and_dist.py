from itertools import combinations


def solution(places):
    answer = [0] * 5
    for i in range(5):
        place = places[i]
        flag = 1

        def get_dist(r1, c1, r2, c2):
            return abs(r1 - r2) + abs(c1 - c2)

        def check(r1, c1, r2, c2):
            if r1 == r2:
                if place[r1][min(c1, c2) + 1] == 'O':
                    return False
            elif c1 == c2:
                if place[min(r1, c1) + 1][c1] == 'O':
                    return False
            else:
                if place[r2][c1] == 'O':
                    return False
                if place[r1][c2] == 'O':
                    return False
            return True

        # P의 위치정보들을 기반으로 완전탐색해야 함. 맨해튼 거리가 2를 초과하면 되는데, 2여도 가능한 케이스가 있음
        people = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    people.append((r, c))
        combs = list(combinations(people, 2))
        for p in combs:
            d = get_dist(p[0][0], p[0][1], p[1][0], p[1][1])
            if d > 2:
                continue
            elif d == 2:
                if not check(p[0][0], p[0][1], p[1][0], p[1][1]):
                    flag = 0
                    break
            else:
                flag = 0
                break
        answer[i] = flag
    return answer