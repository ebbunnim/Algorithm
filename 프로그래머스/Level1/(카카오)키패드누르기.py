def solution(numbers, hand):
    keys = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }
    ans = ''
    left = (3, 0)
    right = (3, 2)

    for num in numbers:
        if num in (2, 5, 8, 0):
            left_dist = abs(keys[num][0] - left[0]) + abs(keys[num][1] - left[1])
            right_dist = abs(keys[num][0] - right[0]) + abs(keys[num][1] - right[1])
            if left_dist < right_dist:
                left = keys[num]
                ans += 'L'
            elif left_dist == right_dist:
                if hand == 'left':
                    left = keys[num]
                    ans += 'L'
                else:
                    right = keys[num]
                    ans += 'R'
            else:
                right = keys[num]
                ans += 'R'
            continue
        if num in (1, 4, 7):
            left = keys[num]
            ans += 'L'
        else:
            right = keys[num]
            ans += 'R'
    return ans