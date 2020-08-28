def solution(s):
    L = len(s)

    def is_pal(sub_s):
        for i in range((len(sub_s)) // 2):
            if sub_s[i] != sub_s[-i - 1]:
                return False
        return True

    for i in range(L, 0, -1):
        for j in range(L):
            if j + i - 1 >= L:
                break
            if is_pal(s[j:j + i]):
                return i
    return 1