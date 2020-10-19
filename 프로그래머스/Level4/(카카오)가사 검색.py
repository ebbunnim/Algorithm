from collections import defaultdict


def solution(words, queries):
    def get_lower_bound(fit_words, target):  # from fit_words, set target to lower bound
        s, e = 0, len(fit_words)  # 1개 원소일때도 이분탐색 할 수 있도록 e 설정
        while s < e:
            mid = (s + e) // 2
            if fit_words[mid] >= target:
                e = mid
            else:
                s = mid + 1
        return e

    def get_upper_bound(fit_words, target):
        s, e = 0, len(fit_words)
        while s < e:
            mid = (s + e) // 2
            if fit_words[mid] > target:
                e = mid
            else:
                s = mid + 1
        return e

    word_dict = defaultdict(list)
    reverse_word_dict = defaultdict(list)

    for word in words:
        word_dict[len(word)] += [word]
        reverse_word_dict[len(word)] += [word[::-1]]
    for key in word_dict:
        word_dict[key].sort()
        reverse_word_dict[key].sort()

    result = [0] * len(queries)
    for i in range(len(queries)):
        if queries[i][0] != '?':
            lo = get_lower_bound(word_dict[len(queries[i])], queries[i].replace('?', 'z'))
            hi = get_upper_bound(word_dict[len(queries[i])], queries[i].replace('?', 'a'))
            result[i] = lo - hi
        else:  # from reverse_word_dict
            lo = get_lower_bound(reverse_word_dict[len(queries[i])], queries[i][::-1].replace('?', 'z'))
            hi = get_upper_bound(reverse_word_dict[len(queries[i])], queries[i][::-1].replace('?', 'a'))
            result[i] = lo - hi

    return result
